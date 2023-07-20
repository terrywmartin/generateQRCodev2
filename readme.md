# generateQrCode

Generate a QR Code for a URL, a vCard, or WiFi connection.  Select the type of QR code you want to generate, enter the information, then hit 'Generate'.   A QR Code will displayed along with a download button.

This project uses Django, HTMx, and Alpine.js.  HTMx gives the app a SPA feel while Alpine.js hides the forms until the corresponding button is clicked.

TODO:

 - Add better error handling
 - Add comments
 - Add Tests
 - Ready for deployment

I first saw this idea on Traversy Media's YouTube page.  He made this using Html/Tailwind CSS/Javascript.  I wanted to see if I could do it using Django.  I did this in a couple of hours.  I'm terrible at front-end so it's not very polished, but it works.  I'm sure there a few places in the code that could use improving but I was really focused on getting it done quickly.  

I am still learning so forgive the crudeness of the code.

## To run the project

Create your virtual environment using the method of you choice.  I use venv.

Install dependencies in your virtual environment.

```
pip install -r requirements.txt
```

Run the project.

```
py manage.py runserver
```
