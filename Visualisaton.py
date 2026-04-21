import streamlit as st
import streamlit.components.v1 as components

# 1. Налаштування сторінки
st.set_page_config(page_title="Міграційні тенденції", layout="wide")

# --- СТИЛІЗАЦІЯ ВКЛАДОК (TABS) ---
st.markdown("""
    <style>
    /* Збільшуємо шрифт назв регіонів у вкладках */
    button[data-baseweb="tab"] p {
        font-size: 18px !important;
        font-weight: 600 !important;
        transition: all 0.3s ease;
    }

    /* Стиль для ОБРАНОЇ вкладки (синій квадратик/фон) */
    button[data-baseweb="tab"][aria-selected="true"] {
        background-color: #007bff !important; /* Насичений синій */
        color: white !important;
        border-radius: 8px 8px 0px 0px !important;
        padding: 10px 20px !important;
    }

    /* Зміна кольору тексту обраної вкладки на білий */
    button[data-baseweb="tab"][aria-selected="true"] p {
        color: white !important;
    }

    /* Стиль при наведенні курсору */
    button[data-baseweb="tab"]:hover {
        background-color: rgba(0, 123, 255, 0.1) !important;
        border-radius: 8px !important;
    }
    </style>
""", unsafe_allow_html=True)


# Функція для вставки iframe
def dw_chart(url, height=750):
    components.html(
        f"""
        <div style="padding: 10px;">
            <iframe src="{url}" 
                    scrolling="no" 
                    frameborder="0" 
                    style="border: none; width: 100%; height: {height}px;">
            </iframe>
        </div>
        """,
        height=height + 50
    )


# Виправлена функція для великого тексту без помилок відображення HTML
def display_big_text(content):
    st.markdown(f'<p style="font-size: 20px; line-height: 1.6; margin-bottom: 20px;">{content}</p>',
                unsafe_allow_html=True)


# 2. Головний заголовок
st.markdown("""
    <div style="background-color: #1a2a3a; padding: 25px; border-radius: 10px; text-align: center; margin-bottom: 40px;">
        <h1 style="color: white; margin: 0;">Міграційні тенденції</h1>
        <p style="color: #cccccc; font-size: 1.2rem;">Візуалізація даних про міжнародну міграцію</p>
    </div>
""", unsafe_allow_html=True)

# 3. Блок 1: Світова карта
st.header("Зосередження мігрантів у світі")
col_map1, col_txt1 = st.columns([1.8, 1])

with col_map1:
    dw_chart("https://datawrapper.dwcdn.net/V5G9Z/1/", height=500)

with col_txt1:
    st.write("##")
    display_big_text(
        "Карта демонструє розподіл міжнародних мігрантів за основними регіонами світу. Найбільша концентрація спостерігається в Європі та Азії.")

st.divider()

# 4. Блок 2: Детальний аналіз за регіонами
st.header("Детальний аналіз за регіонами")
regions = ["Європа", "Азія", "Північна Америка", "Південна Америка", "Африка", "Океанія"]
urls = [
    "https://datawrapper.dwcdn.net/yWfM8/1/",
    "https://datawrapper.dwcdn.net/uPUWn/1/",
    "https://datawrapper.dwcdn.net/iZseD/1/",
    "https://datawrapper.dwcdn.net/0HIfD/1/",
    "https://datawrapper.dwcdn.net/5lHVX/1/",
    "https://datawrapper.dwcdn.net/TdhfV/1/"
]
texts = [
    "Регіон з найвищою концентрацією внутрішньорегіональної міграції. Спільний ринок праці та спрощений перетин кордонів сприяють активному руху населення між країнами ЄС.",
    "Азія демонструє найшвидші темпи зростання міграційних потоків. Це зумовлено як економічним стрибком окремих країн, так і великою кількістю трудових мігрантів.",
    "Традиційний лідер за кількістю іммігрантів. Міграційні процеси тут мають історично сталий характер і значною мірою впливають на ринок праці.",
    "Регіон характеризується значними потоками всередині континенту, що часто спричинені політичною нестабільністю або економічними кризами.",
    "Міграція в Африці часто має вимушений характер через конфлікти або кліматичні зміни, проте спостерігається і тенденція економічної міграції.",
    "Попри невелику загальну кількість людей, регіон має один із найвищих у світі показників мігрантів на душу населення."
]

tabs = st.tabs(regions)

for i in range(len(regions)):
    with tabs[i]:
        c1, c2 = st.columns([1.8, 1])
        with c1:
            dw_chart(urls[i], height=750)
        with c2:
            st.write("##")
            st.subheader(f"Особливості регіону: {regions[i]}")
            display_big_text(texts[i])

st.divider()

# 5. Блок 3: Динаміка
st.header("Аналітика та динаміка")
dw_chart("https://datawrapper.dwcdn.net/BmtjW/1/", height=550)
display_big_text("Ця візуалізація демонструє зміну частки мігрантів у світі протягом років.")

dw_chart("https://datawrapper.dwcdn.net/pRxv4/2/", height=250)
display_big_text("Графік відображає частку мігрантів у загальній структурі населення кожного регіону.")

# 6. Футер
st.info("Практична робота з візуалізації даних. Виконано за допомогою Python та Datawrapper.")