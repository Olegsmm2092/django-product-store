# Django Product Store with Customers
This is a Django-based web application for managing a product store with customer information. The application utilizes an object-oriented approach to design and implement the functionality.

## Features
* Customer Management: The application allows you to create, view, update, and delete customer records. Each customer record contains information such as customer name, password, country, city, street, and house.

* Product Management: You can easily extend the application to include product management functionality, enabling you to add, update, and delete product records.

* User Authentication: The application provides user authentication functionality, allowing customers to create accounts, log in, and log out securely.

* Search and Filtering: Customers can search for specific products based on various criteria, such as product name, category, or price range.

* Shopping Cart: The application supports a shopping cart feature, allowing customers to add products to their cart, view the contents, and proceed to checkout.

## Object-Oriented Design
The Django Product Store with Customers application follows an object-oriented design approach, leveraging Django's model-view-controller (MVC) architecture.

* Models: The core business entities, such as customers and products, are represented as Django models. These models encapsulate the data and behavior associated with the entities.

* Views: The views handle user interactions, retrieve data from the models, and render templates to present the data to the users. They also handle form submissions, authentication, and other logic related to customer management.

* Templates: The application utilizes Django templates to generate dynamic HTML pages based on the provided data. The templates provide a user-friendly interface for interacting with the application.

* Forms: Django forms are used for validating user input, such as when creating or updating customer records. The forms enforce data integrity and provide a convenient way to handle form submissions.

* Authentication: Django's built-in authentication system is used to handle user registration, login, and logout. This ensures secure access to the application's features and protects customer information.

## Getting Started
To get started with the Django Product Store with Customers application, follow these steps:

1. Clone the repository to your local machine:

    ````bash
    git clone https://github.com/Olegsmm2092/django-product-store.git
    ````
2. Install the required dependencies by creating and activating a Python virtual environment:

    ````bash
    virtualenv -p python3.11 venv
    ````
    ````bash
    source venv/Script/activate
    ````
    ````bash
    pip install -r requirements.txt
    ````

3. Set up the database by applying the migrations:

    ````bash
    python manage.py migrate
    ````
4. Start the development server:

    ````bash
    python manage.py runserver
    ````
    The application will be accessible at http://127.0.0.1:8000/.

5. Explore the different features of the application, create customer records, and manage products as per your requirements.

## Usage
1. Access the customer management system by visiting http://localhost:8000/customers.

2. Create a new customer by clicking on the "Create Customer" button and filling out the form.

3. Update or delete a customer by clicking on the respective buttons next to each customer in the list.

4. View the details of a customer, including their associated products, by clicking on the customer's name.


## Implement the Framework Functionality
1. Structure for the templates directory:

    ````hljs
    ├── templates/
    │   └── main/
    │       ├── base.html
    │       ├── product_list.html
    │       ├── product_create.html
    │       ├── product_detail.html
    │       ├── product_update.html
    │       └── product_confirm_delete.html
    │            ...
    ├── urls.py
    └── views.py
        ...
    ````

## Contributing
Contributions to the Django Product Store with Customers project are welcome. If you find any issues or have ideas for improvements, please submit a pull request or open an issue in the GitHub repository.

## License
The Django Product Store with Customers application is open-source and released under the MIT License. Feel free to modify and use it according to your needs.

## Acknowledgments
This project was built using Django, a high-level Python web framework. Special thanks to the Django community for their excellent documentation and support.

## Contact
For any inquiries or questions, please contact olegsobadov@gmail.com.