from strands import Agent
from strands.models import BedrockModel
from strands_tools import editor, file_write
from termcolor import colored


def writer_team(market_research: str, project_description: str):
    response = str()
    try:
        content_writer = Agent(
            system_prompt="""Develop and revise compelling and innovative content, including campaign ideas,
            campaing copy, and even detailed campaign reports. As a Content Writer at a digital marketing agency, you 
            excel in creating narratives that resonate with target audiences. 
            Your expertise is in turning marketing strategies into engaging stories and visual 
            content that captures attention and inspires action.
            """,
            # model=BedrockModel(
            #     model_id="us.anthropic.claude-3-5-haiku-20241022-v1:0",
            # ),
        )

        formatted_report_writer = Agent(
            system_prompt="""Produce and save a markdown-formatted report based on all of the outputs of your team's work and the project's description. As a Report Writer you are excellent at taking everyone else's great work and 
            producing a cleanly formatted and easily readable report, saved in Markdown format 
            using file_write and editor tool. Create the file in current directory.""",
            # model=BedrockModel(
            #     model_id="us.anthropic.claude-3-5-haiku-20241022-v1:0",
            # ),
            tools=[file_write, editor],
        )


        print(colored("\n### Content Writer is working! ###\n", "yellow"))

        content_writer_response = str(content_writer(market_research))


        print(colored("\n### Report Writer is working! ###\n", "yellow"))
        response = str(formatted_report_writer(f"Project description: \n\n{project_description}\n\n" + content_writer_response))


        if len(response) > 0:
            return response

        return "I apologize, but I couldn't properly analyze your question. Could you please rephrase or provide more context?"

    # Return specific error message for English queries
    except Exception as e:
        return f"Error processing your query: {str(e)}"
