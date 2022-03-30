import pdfkit
import streamlit as st
from jinja2 import Environment, FileSystemLoader, select_autoescape

st.set_page_config(layout="centered", page_icon="💰", page_title="Invoice Generator")
st.title("💰 Invoice Generator")

st.write(
    "This app shows how you can use Streamlit to make an invoice generator app in just a few lines of code!"
)


env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
template = env.get_template("invoice_template.html")


with st.form("template_form"):
    left, right = st.columns((1, 10))
    color = left.color_picker("Color", value="#b4cffa")
    company_name = right.text_input("Company name", value="SkiFoo")
    left, right = st.columns(2)
    customer_name = left.text_input("Customer name", value="Slope Corporation")
    customer_address = right.text_input("Customer address", value="Red skiing runs")
    product_type = left.selectbox("Product type", ["Data app crafting", "ML model training"])
    quantity = right.number_input("Quantity", 1, 10)
    price_per_unit = st.slider("Price per unit", 1, 100, 60)
    total = price_per_unit * quantity
    submit = st.form_submit_button()

if submit:
    html = template.render(
        color=color,
        company_name=company_name,
        customer_name=customer_name,
        customer_address=customer_address,
        product_type=product_type,
        quantity=quantity,
        price_per_unit=price_per_unit,
        total=total,
    )

    pdf = pdfkit.from_string(html, False)
    st.balloons()

    st.success("🎉 Your invoice was generated!")

    st.download_button(
        "⬇️ Download PDF",
        data=pdf,
        file_name="invoice.pdf",
        mime="application/octet-stream",
    )
