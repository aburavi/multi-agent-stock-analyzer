import streamlit as st
from streamlit.runtime.scriptrunner import get_script_run_ctx
import os
import markdown
import pdfkit

from config import settings
from agents_tasks import crewapi
from custom_tools import send_report

def generate_report(company_name):
    crew_output = crewapi.kickoff(inputs={"company_stock": company_name})
    st.session_state['crew_output'] = crew_output

    markdown_text = crew_output.raw
    with open("stock_report.txt", "w") as f:
        f.write(markdown_text)

    html = markdown.markdown(markdown_text)
    with open("stock_report.html", "w") as f:
        f.write(html)

    try:
        config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')
        pdfkit.from_file("stock_report.html", "stock_report.pdf", configuration=config)
    except Exception as e:
        st.error(f"PDF generation failed: {e}")

def display_report(company_name):
    st.markdown(st.session_state['crew_output'].raw)
    with st.expander("Show Chain of Thought"):
        for task in st.session_state['crew_output'].tasks_output:
            st.markdown(f"**{task.name}**: {task.raw}")
        st.write("**Token Usage**:", st.session_state['crew_output'].token_usage)

    email_address = st.text_input("Enter your email", "")
    if st.button("Send Email") and email_address:
        send_email(company_name, email_address)

def send_email(company_name, email_address):
    sender_email = os.getenv('SENDER_EMAIL')
    receiver_email = email_address
    password = os.getenv('EMAIL_PASSWORD')
    subject = f"Stock Analysis Report: {company_name}"
    body = "Please find the attached stock analysis report."
    file_name = "stock_report.pdf"

    try:
        send_report(sender_email, receiver_email, password, subject, body, file_name)
        st.success(f"Email sent successfully to {email_address}!")
    except Exception as e:
        st.error(f"Failed to send email: {e}")

def main():
    st.title("Stock Analysis Report Generator")

    ctx = get_script_run_ctx()
    if ctx is None:
        st.warning("⚠️ No ScriptRunContext — you’re outside Streamlit execution!")
    else:
        st.success("✅ ScriptRunContext is active")

    if 'report_generated' not in st.session_state:
        st.session_state['report_generated'] = False
    if 'crew_output' not in st.session_state:
        st.session_state['crew_output'] = None

    company_name = st.text_input("Enter Company Name or Stock Ticker", "")

    if st.button("Generate Report"):
        if not company_name.strip():
            st.error("Please enter a valid company name or stock ticker.")
            st.session_state['report_generated'] = False
        else:
            with st.spinner("Generating stock analysis report..."):
                generate_report(company_name)
            st.success(f"Report for {company_name} generated successfully!")
            st.session_state['report_generated'] = True

    if st.session_state['report_generated'] and st.session_state['crew_output']:
        display_report(company_name)

if __name__ == "__main__":
    main()