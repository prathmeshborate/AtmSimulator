# AtmSimulator
An ATM Simulator created using Python and MySQL for simulating basic ATM functionalities.

![ATM Simulator Screenshot](AtmSimulator.PNG)

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Setup](#steup)
  - [Prerequisites](#prerequisites)
  - [Database Setup](#database-setup)
  - [Running the ATM Simulator](#running-the-atm-simulator)
- [Usage](#usage)
- [Contribution](#contribution)

---

## Project Overview

The ATM Simulator is a Python-based application that emulates a basic ATM interface. It allows users to perform common banking operations, including checking their account balance, making withdrawals, and depositing funds.

## Features

- User authentication using a card number and PIN.
- Account balance inquiry.
- Cash withdrawal and deposit options.
- Real-time updates to the available balance.
- User-friendly command-line interface.

## Setup

### Prerequisites

Before running the ATM Simulator, ensure you have the following components installed:

- Python 3.x
- MySQL (or another database of your choice)

### Database Setup

1. **Create a MySQL Database:**

   Create a new MySQL database named `atmTransaction` using your preferred MySQL management tool or the command line:

   ```sql
   CREATE DATABASE atmTransaction;

2. **Use the Database:**

   Switch to the newly created database:

   ```sql
   USE atmTransaction;

3. **Create the `accountHolder` Table:**

   Define the table structure for storing account holder information, including card numbers, PINs, and available balances:
   
   ```sql
   CREATE TABLE accountHolder (
    cardNo INT PRIMARY KEY,
    cardPin INT NOT NULL,
    availBalance DECIMAL(10, 2) DEFAULT 0.0
   );

5. **Add Sample Account Holder Data**
   
   You can add sample account holder data to the `accountHolder` table to get started. Here's an example:
   
   ```sql
   -- Insert sample account holder data
   INSERT INTO accountHolder (cardNo, cardPin, availBalance)
   VALUES
      (1234567890123456, 1234, 1000.00),
      (2345678901234567, 5678, 500.50),
      (3456789012345678, 9876, 250.75);

### Running the ATM Simulator

1. Clone the repository:
   ```bash
   git clone https://github.com/prathmeshborate/AtmSimulator.git

2. Navigate to the project directory:
   ```bash
   cd AtmSimulator

3. Run the ATM Simulator:
   ```bash
   python main.py

## Usage

1. Launch the ATM Simulator.
2. Follow the on-screen instructions to log in using your card number and PIN.
3. Use the available options to perform ATM operations.

## Contribution

Contributions to the ATM Simulator project are welcome! You can contribute by:

- Adding new features or enhancements.
- Fixing bugs and issues.
- Improving code quality and documentation.
