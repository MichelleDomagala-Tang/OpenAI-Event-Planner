# OpenAI Event Planner Application

This app utilizes OpenAI APIs to generate schedules and help plan for large events. This includes planning large meetings, weddings, or vacations that often require a lot of planning and coordination.

*(Note that although OpenAI is integrated, the app is still under development)*

![Homepage](/static/Homepage.png)

## Motivation
After witnessing how difficult it is to plan large events like weddings or coorporate meetings, I saw an opportunity to make an app. This event planner application uses responses from OpenAI APIs to create a starting point, list what needs to be completed, and help create an itinerary for any type of event.

## Running the Application
This application runs off Python (Flask). The following commands will run the application:
```
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
flask run
```
Note that a working OpenAI API Key is needed to run the application. A key can be added by following the [OpenAI Documentation](https://platform.openai.com/docs/quickstart/build-your-application).