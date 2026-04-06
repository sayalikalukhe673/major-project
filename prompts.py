""" prompts  templates for AI support assistance."""

system_prompt = """ you are a helpful anf professional customer support
assistance
your goal is to provide accurate ,clear,and friendly response to cuctomer
question.
always be polite,concise, helpful. if tou don't know the answer ,say so
honestly."""


QA_prompt_template = """Question :{function}

please provide a clear and helpful answer to the customer's question above.
keep your response professinal and easy to understand."""

SUMMARY_PROMPT_TEMPLATE = """please summarize the following text  in c clear
and concise way:

{text}

provide a brief that capture the main points."""


CONTEX_QA_PROMPT_TEMPLATE = """ use the following  contex to answer the 
cistomer's question.
if the contex doesn't containt the answer ,say that you don't heve enough information.

Contex:
{contex}


Question {question}

pleaase provide a helpful answer based on contex above"""