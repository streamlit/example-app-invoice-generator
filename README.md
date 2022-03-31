# 💰 Invoice Generator

A Streamlit app to show how you can easily use Streamlit to generate invoices as PDFs.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/streamlit/example-app-invoice-generator/main)

<table border="0">
    <tr>
        <td>App screenshot</td>
        <td>Invoice template</td>
    </tr>
    <tr>
        <td><img width="400" alt="image"
                src="https://user-images.githubusercontent.com/7164864/160867685-b0992150-b194-4cf4-81af-62bbbf057dc3.png">
        </td>
        <td><img width="400" alt="image"
                src="https://user-images.githubusercontent.com/7164864/160867815-a80fca43-7f1d-4f61-96ab-3cdf3eba4cfd.png">
        </td>
    </tr>
</table>

### How to run this demo
The demo has been deployed using Python 3.7. **We suggest creating a new virtual environment**, then running:

```
git clone https://github.com/streamlit/example-app-invoice-generator.git
cd example-app-invoice-generator
pip install -r requirements.txt
streamlit run streamlit_app.py
```

### About the app

- Code is powered by <a href="https://streamlit.io"> Streamlit</a> 🎈 and deployed on [Streamlit Cloud](https://streamlit.io/cloud) ☁️
- It is super compact: only 50 lines of code. Check it out in [`streamlit_app.py`](https://github.com/streamlit/example-app-invoice-generator/blob/main/streamlit_app.py)

### About the template
   
- Template must be an HTML file with <code>{{ my_variable }}</code> variable placeholders as supported by [jinja](https://jinja.palletsprojects.com/en/3.1.x/). 
- Our example template here is [`invoice_template.html`](https://github.com/streamlit/example-app-invoice-generator/blob/main/invoice_template.html) and you can see placeholders e.g. [here](https://github.com/streamlit/example-app-invoice-generator/blob/main/invoice_template.html#L329).
   
🪄 Tip: if you're not an HTML expert (or if you're lazy, or both) just kick-off your template using Google Docs at <a href="https://docs.new">docs.new</a> and then export it as HTML using <kbd>File</kbd> > <kbd>Download</kbd> > <kbd>Web page (.html, zipped)</kbd>. For example, this is our original <a href="https://docs.google.com/document/d/1ekg49TXzQfolnEw-czBo7pDVmOTyAkr6EsKs-_h-kq0/edit"> template in Google Docs!

### Questions? Comments?

Please ask in the [Streamlit community](https://discuss.streamlit.io).
