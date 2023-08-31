# Profiles REST API

Profiles REST API course code.

Architectural Flow:
- User makes a request -> HTTP request is sent to a specific URL
- Django's URL dispatcher matches the URL request to a specific view function based on the URL patterns defined in urls.py
- The view function is responsible for processing this request and returning an appropriate HTTP response
- In the view function, code is written for the views to interact with the models (data models) to fetch, update or manipulate data.
- Using in-built serializer libs, the serializer classes can be used to convert model data into data types such as JSON, that is readable by the front-end
- The respective view function returns an HTTP response, which could be HTML template rendered with data or serialized JSON response.
- If i've registered my models with the in-built admin interface, i can also manage my app data using the admin site interface.