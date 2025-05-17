# Coffee-Shop-Challenge

## Description
This is a Python project simulating a coffee shop domain featuring Customer, Coffee, and Order models. 
The system captures the relationships between these entities such as customers placing orders for different coffee types and tracks relevant data like order prices and customer's preference.
This repository contains the implementation of a domain model for a coffee shop, including relationships, aggregates, and optional bonus features, developed as part of a code challenge. 
The project uses pytest for testing and GitHub Actions for continuous integration.

## Overview
This project simulates a coffee shop domain with three core models:
-*Customer*: Represents a customer with a name and order history.
- *Coffee*: Represents a coffee type with order associations.
- *Order*: Links a customer to a coffee with a price.

The models enforce specific validations, maintain relationships (many-to-many between Coffee and Customer via Orders), and provide aggregates like order counts and average prices. An optional bonus feature identifies the customer who spends the most on a given coffee.

## Features
- *Model Validations*:
  - Customer name: String, 1–15 characters.
  - Coffee name: String, ≥3 characters, immutable.
  - Order price: Float, 1.0–10.0, immutable.
- *Relationships*:
  - Order.customer and Order.coffee (type-checked).
  - Customer.orders() and Customer.coffees() for order and coffee history.
  - Coffee.orders() and Coffee.customers() for order and customer associations.
- *Aggregates*:
  - Customer.create_order(coffee, price) to instantiate orders.
  - Coffee.num_orders() for order count.
  - Coffee.average_price() for mean order price.
- *Bonus Feature*:
  - Customer.most_aficionado(coffee): Class method to find the top-spending customer for a coffee.
- *Testing*: Comprehensive unit tests with pytest.
  

## Setup
To get started with the project locally, follow these steps:

1. *Clone the Repository*:

   git clone git@github.com:Joykinuthia/coffee-shop-challenge.git
   cd coffee-shop-challenge
   
## Install Dependencies
Install project dependencies:
pipenv install
pipenv shell

Verify Environment:
This project requires Python 3.9+. The Pipfile ensures compatibility.

## Usage
Running the Debug Script.
Test the application manually:
python debug.py

## License
This project is licensed under the MIT License. 

## Authors
Joyrose Kinuthia
