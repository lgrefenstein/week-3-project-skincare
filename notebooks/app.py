import streamlit as st
import pandas as pd
import plotly.express as px

st.markdown("""
    <style>
    [data-testid="stMetricValue"],
    [data-testid="stMetricLabel"] {
        width: fit-content;
        margin: auto;
    }
    [data-testid="stMetricValue"] {
        font-size: 2rem;
    }
    [data-testid="stMetricLabel"] {
        font-size: 1.2rem;
    }
    </style>
""", unsafe_allow_html=True)

st.set_page_config(
    page_title="Clean Beauty Reality Check",
    page_icon="🧴"
)

ingredient_info = {
    'Fragrance / Parfum': {
        'description': 'A general term for a mixture of aromatic compounds added to give a pleasant scent. Can contain dozens of individual chemicals not individually disclosed.',
        'purpose': 'Makes products smell good!',
        'concern': 'One of the most common causes of contact allergy in cosmetics. The EU requires individual labeling of 80+ specific fragrance allergens when present above certain thresholds.'
    },
    'Limonene': {
        'description': 'A naturally-occurring compound found in citrus peels (lemon, orange) and many essential oils. Often used as a fragrance ingredient.',
        'purpose': 'Adds citrus scent; also used as a solvent.',
        'concern': 'EU-listed fragrance allergen. Can oxidize over time and become more irritating, especially for people with sensitive skin.'
    },
    'Linalool': {
        'description': 'A floral-smelling alcohol naturally found in lavender, mint, and many other plants. Widely used in fragrances.',
        'purpose': 'Adds floral scent.',
        'concern': 'EU-listed fragrance allergen. Oxidized linalool is a common cause of contact dermatitis.'
    },
    'Citronellol': {
        'description': 'A naturally-occurring scent compound found in rose and geranium oils.',
        'purpose': 'Adds rose/floral scent.',
        'concern': 'EU-listed fragrance allergen, though generally lower-risk than some others.'
    },
    'Geraniol': {
        'description': 'A floral alcohol found in rose and geranium oils.',
        'purpose': 'Adds rose scent.',
        'concern': 'EU-listed fragrance allergen. Can cause contact allergic reactions.'
    },
    "Alcohol Denat": {
        'description': 'Ethanol that has been made undrinkable by adding bitter substances. The most common "drying alcohol" in skincare.',
        'purpose': 'Solvent, quick-drying feel, helps other ingredients absorb faster.',
        'concern': 'Can strip moisture from skin, causing dryness and irritation. More problematic in leave-on products and for dry or sensitive skin. Generally fine in small amounts or rinse-off products.'
},

    "Ethanol": {
        'description': 'Pure alcohol, sometimes listed as "Ethyl Alcohol." The same alcohol found in alcoholic drinks, used in cosmetics as a solvent.',
        'purpose': 'Solvent, preservative, creates lightweight texture.',
        'concern': 'Same concern as Alcohol Denat. It can dry and irritate skin at high concentrations. Often found in toners, essences, and sunscreens.'
},

    "Benzyl Alcohol": {
        'description': 'A naturally occurring aromatic alcohol found in many fruits and teas. Used in cosmetics primarily as a preservative.',
        'purpose': 'Preservative: Prevents bacterial growth in products.',
        'concern': 'Milder than other drying alcohols but still an EU-listed fragrance allergen. Can cause irritation or allergic reactions in sensitive individuals. Often used as a "cleaner" alternative to parabens.'
},

    'SLS (Sodium Lauryl Sulfate)': {
        'description': 'A strong surfactant (cleansing agent) commonly used in cleansers, shampoos, and toothpastes.',
        'purpose': 'Creates lather and removes oil/dirt.',
        'concern': 'Well-documented skin irritant, especially in leave-on products or for sensitive skin. Generally safer in rinse-off products.'
    },

    'Phenoxyethanol': {
        'description': 'A synthetic preservative used in cosmetics to prevent bacterial and fungal growth. One of the most common preservatives in skincare since parabens fell out of favor.',
        'purpose': 'Preservative: Prevents products from spoiling.',
        'concern': 'Generally considered safe at low concentrations (EU limit: 1%), but can cause irritation or allergic reactions in some people, especially those with sensitive skin. It is frequently flagged by "clean beauty" brands despite being one of the safer preservative options available.'
}}


df = pd.read_csv('products_with_scores.csv')


st.title("🧴 Clean Beauty Reality Check")
st.markdown("---")
st.header("🔍 Irritant Ingredients Explorer")
st.write("Pick an ingredient and find out more:")

search_term = {
    'Fragrance / Parfum': 'fragrance|parfum',
    "Phenoxyethanol": "phenoxyethanol",
    'Limonene': 'limonene',
    'Linalool': 'linalool',
    'Citronellol': 'citronellol',
    'Geraniol': 'geraniol',
    'Alcohol Denat': 'alcohol denat',
    'Ethanol': 'ethanol',
    'Benzyl Alcohol': 'benzyl alcohol',
    'SLS (Sodium Lauryl Sulfate)': 'sodium lauryl sulfate',
}

selected = st.pills(
    "",
    list(ingredient_info.keys()),
)

if selected:
    info = ingredient_info[selected]

    st.info(f"""
    **What is it?** {info['description']}

    **Purpose:** {info['purpose']}

    **Why it's on our list:** {info['concern']}
    """, icon="ℹ️")

    search_term = search_term[selected]
    contains = df[df['Ingredients'].str.contains(search_term, case=False, na=False)]

    total = len(df)
    clean_total = (df['Clean Product'] == True).sum()
    regular_total = (df['Clean Product'] == False).sum()
    total_with = len(contains)
    clean_with = (contains['Clean Product'] == True).sum()
    regular_with = (contains['Clean Product'] == False).sum()

    _, center_col, _ = st.columns([1, 5, 1])

    with center_col:
        col1, col2, col3 = st.columns(3)
        col1.metric("Products containing it", f"{(total_with / total) * 100:.0f}%")
        col2.metric("Clean products with it", f"{(clean_with / clean_total) * 100:.0f}%")
        col3.metric("Conventional products with it", f"{(regular_with / regular_total) * 100:.0f}%")


    clean_pct = round((clean_with/clean_total)*100)
    regular_pct = round((regular_with/regular_total)*100)

    if clean_pct > regular_pct:
        st.error(f"⚠️ {selected} is found more frequently in clean products ({clean_pct:.0f}%).")
    elif clean_pct == regular_pct:
        st.warning(f"🚨 {selected} appears at a similar rate in both clean and conventional products.")
    else:
        st.success(f"✅ {selected} is found less frequently in clean products ({clean_pct:.0f}%).")


    with st.expander(f"See all {clean_with} Clean products containing {selected}"):
        st.dataframe(contains[contains["Clean Product"] == True][['Product Name']], hide_index=True)


st.markdown("---")
st.header("📊 What Does the Data Say?")


clean_avg = df[df['Clean Product']==True]['irritation_score'].mean()
regular_avg = df[df['Clean Product']==False]['irritation_score'].mean()

_, center_col, _ = st.columns([1, 5, 1])

with center_col:
    col1, col2 = st.columns(2)
    col1.metric("Avg number of irritants in clean products", f"{clean_avg:.1f}")
    col2.metric("Avg number of irritants in conventional products", f"{regular_avg:.1f}")


fig = px.histogram(
    df,
    x="irritation_score",
    color="Clean Product Label",
    barmode="group",  # equivalent to "dodge" in seaborn
    title="Distribution of Irritation Scores"
)

fig.update_xaxes(title="Irritation Score")
fig.update_yaxes(title="Number of Products")

st.plotly_chart(fig, use_container_width=True)