# Elderly Care Chatbot Project

## Introduction

This project aims to develop a chatbot specifically designed to assist and engage elderly individuals. The chatbot is intended to provide support, companionship, and information to the elderly, enhancing their overall well-being and quality of life.

## Features

- **Conversation Assistance**: The chatbot can engage in conversations with the elderly users, providing companionship and mental stimulation.
- **Information Retrieval**: The chatbot can retrieve information on various topics like health tips, local events, weather, and more.
- **Reminders and Alerts**: The chatbot can set reminders for medication, appointments, and other important events for the elderly users.
- **Emergency Assistance**: The chatbot is equipped to handle emergency situations by providing relevant information and guiding the user on necessary actions.
- **Database Integration**: Utilizes a PostgreSQL (Postgres) database to store user information, chat history, and other relevant data.
- **OpenAI API Integration**: Utilizes the OpenAI API to generate human-like responses and enhance the conversational experience for the users.

## Prerequisites

Before running the chatbot, ensure you have the following prerequisites:

1. **OpenAI API Key**: Obtain an API key from OpenAI to utilize the GPT-3.5 model for generating responses.
2. **PostgreSQL Database**: Set up a PostgreSQL database to store user data, chat history, and other necessary information.

## Setup

Navigate to the project directory:

`cd elderly-care-chatbot`

Install the required dependencies:

`pip install -r requirements.txt`

Configure the PostgreSQL database connection in the testdb.py file.

Set your OpenAI API key in the action.py file.

## Usage

### Run the chatbot application:

- Use 2 terminals

One to run actions:

`rasa run actions`

The other to run chatbot shell:

`rasa shell`




