# The Recipe Database

  
The live site is [here](https://the-recipe-db.herokuapp.com/).

A recipe sharing site for foodies!

____

## Description

This site is created for people who like to cook and discover new recipes.  Users are able to save their own recipes in their own online cookbook "My Cookbook".  Along with access to their own recipes, users can find recipes for all other users via the recipes page on the web site.  

## Purpose

Along with being a convenient  place for people to safely store their own recipes,  as the the database grows, it will become a significant free online resource for foodies to find new recipes to try.
____

## User Stories

### User

*"I want a website that I can navigate easily.”
“I want to be able to have my own profile.”
“I want to be able to filter between search results”
“I want to be able to upload my own recipes”
“I want to be able to amend or delete my recipes”
“I want to be able to use the site on mobile devices”*

____

## UX

### **Strategy**

#### Owner

- provide a site that users learn to navigate intuitively.
- build up a database of users.
- generate repeat visitors.
- create a mailing list for registered users, to be used to provide information about the site and marketing.

#### User

- To be able to create their own account.
- To find recipes that they would like to try.

### **Scope**

The site will have the following:

 - Allow users to create and delete their account.
 - A place for users to store their own recipes within one place on the site
 - Functionally for the user to be able to update and also delete their  own recipes.
 - A place for users to be able to see and search for all the recipes created by other users.
 - A landing page with a sample of the recipes on the database to encourage non-registered users to sign up
 - 
The front-end will be written in HTML and CSS and will use Bootstrap's grid system and for some of the templates (such as for forms and the navbar).  Any JavaScript in the front end is provided by Bootstrap.

The back-end will be written in Python, also using Flask and Jinja templates.

 All data will be stores in a NoSQL database (mongoDB) 

 #### Scheme

 *User
 _id
:
idnumber will go here
username
:
"John"
email
:
"Johny@fake.co.uk"
password 
:
"Pasword wil be salted by Wverkzoid"

* Recipe:

_id
:
id number will go here
recipe_name
:
"Strawberry cheesecake in a jar"
description
:
"Revolutionise your picnics with this portable cheesecake in a jar! Fre..."
instructions
:
"Stir together biscuit crumbs, butter and 2 tablespoons sugar in a bowl..."
ingredients
:
"6 shortbread biscuits
30g butter, melted
2 tablespoons caster sugar
..."
cooking_time
:
"150"
type
:
"Breakfast"
image
:
"http:."
image_alt
:
""
created_by
:
"user"


### **Structure**

The site is to be intuitive and simple to use.  Users want to be able to login quickly and access their recipes and/or search for recipes added by others easily.

 - This will be a multi-page site.
 - Navigation bar at the top right.
 - Logged user will have access to the full site, although sign up page will not show in navbar.
 - Logged out/non-registered user will only have access to the home page, login and sign up page.
 - Buttons will be provided within the users own area to allow them to edit and update their recipes and profile.
 


### **Skeleton**

 **Navigation**
The navigation bar will be fixed to the top of the screen.  On the left will be the sites name/logo, which if clicked will link back to the home page.  The navigation links will be on the right and collapse into a burger menu on smaller screens such as mobile phones.

The site will have the following links Home, Recipes, ~~Profile~~, My Cookbook, Login, Sign Up.
Initially I was going to call the users area where they can view their recipes 'Profile', but as I was building the site I decided to rename this 'My Cookbook', as it seemed to fit better with the overall layout of the users profile area and was more semantic.

**Home Page** (visible to all users)
The user will be greeted by a hero background  image, upon which will be a call to action button and text.  The image will only cover 80% to 90% of the view hight so that top of the section below, an an about section called ('Sharing is Caring') will be visible on most screen sizes to encourage the user to scroll.     

Below that section will be a list of three sample recipes from the sites database for the logged out/non-registered user to view.  This is to encourage the user to sign up/login, in order to be able to view the other recipes available and have full functionality of the site 

**Sign Up**
Simple sign up form.  The form will capture the user's username and password.  The form will also capture the users email address to satisfy the owners objective of creating a mailing list. 

Having a registered email address will also help the site owner identify the user in the database, should the user make contact via email.

When entering a password the user will be asked to re-enter their chosen password to help eliminate typographical errors in the password that could prevent the user from accessing their site.
 
A link will also be provided to direct the user to the login page if they already have an account

** Login Page**
Simple login form.  Only username and password will be required to login.  Link provided to take the user to the Sign Up page if they do not have an account.

**My Cookbook**
This page will contain a list of the recipes the user has created.  Buttons will be provided so the user can edit or delete their recipes.  If the user clicks the edit button then user will be taken to a edit recipe page.  

If the user clicks on the recipe text/link they will be taken to an page where they can view the recipe in full.

**Recipes**

This is page where all the recipes held in the database are displayed.  The recipes will be provided in cards and will have an image if the user has linked to one when uploading their recipe.  
**Footer**
Simple footer with link to the sites GitHub Repository and email mailto link.

[Click here for wireframes](docs/wireframes.pdf)

### **Surface**

I have decided to use light pastel colours on the site in the main, with some contrasting blacks on the buttons..  The hero image will be in keeping with this theme.

The colours to be used are corral, grey, white (for some text and buttons), and black.  Red will also be used for any delete buttons and yellow for the search buttons.

Font Families:

 - Pattaya, sans-serif - for the page logo and headings
 - Roboto', sans-serif - for all other text on the page

My initial plan was to use background images on the profile and recipe pages and after trying different images in the end I decided not to have any background images other than the hero image.

#### **Mockup**

![Mockup](assets/docs/mockup.png)

____

## Future Features

Recipe rating.  Users will have the option to rate other peoples recipes out of five stars.  Not everyone would want to have their recipe rated, so this feature would be optional.

A chat message board so that users can communicate with each other to discuss recipes and the like.

A space for advertising on the site so that the owner can generate revenue as the traffic to the site grows.
____

## Technologies

* **HTML**
* **CSS** 
* **Python** 
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)- framework used to build the functionally of the site, with the python language
* [MongoDB](https://www.mongodb.com/) - database used to store all the users data and recipe  information - NoSQL.
* [jinja](https://palletsprojects.com/p/jinja/) - templating languages for python.
* [dsnpython](https://pypi.org/project/dnspython/) - Python tool kit
* [pymongo](https://pypi.org/project/pymongo/) - used to communicate with the mongoDB database.
* [Flask-Pymongo](https://flask-pymongo.readthedocs.io/en/latest/) - helper to communicate with mongoDB
*  [Bootstrap](https://getbootstrap.com/) - Used for the modal, start, rules and reset buttons.  Also used for the Bootstrap grid system to help make the site responsive.
* [Google Fonts](https://fonts.google.com/) - For all the fonts used in this site.
* [FontAwesome](https://fontawesome.com/) - Used to provide the email icon in the footer.
* [Favicon Generator](https://favicon.io/favicon-converter/) - used to create favicon ico file from the background image: bg1.jpg
* [Techsini](http://techsini.com/multi-mockup/index.php) - Used to create the Mockup.
* [balsamiq](https://balsamiq.com/)-For wireframes.
* 
* [Gitpod](https://www.gitpod.io/) - Within the Integrated Development Environment (IDE) used in this project. Gitpod extensions used: Auto Close Tag; Bootstrap 4CDN Snippet for boilerplate and head; HTML Hint; Prettier; Color Picker; Indent-Rainbow; and Code Spell Checker.
* [Git](https://git-scm.com/) - version control technology used in ths project.
* [GitHub](http://github.com/) - Stores repositories and is updated via commits sent to it via Git. 
* [Heroku](https://id.heroku.com/login) - Host the live site.
* [Google Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools) - Used to debug and test the site throughout development.
* [FreeFormatter.com](https://www.freeformatter.com/html-formatter.html) - To make sure code indents and is easy to read.
* [CSS Beautifier](http://minifycode.com/css-beautifier/) - To make sure code is easy to read.
* [Codebeautify.org](https://codebeautify.org/python-formatter-beautifier) To make sure code is correctly formatted and easy to read.

____

## Testing

[Click here for testing information](assets/docs/testing.md)

____

## Deployment

The site is created using Gitpod (IDE) and the site documentation is contained within a repository in GitHub.  The repository can be found [here](https://github.com/Bradders81/ms2-memory-game)

The files, documents were sent to GitHub from Gitpod, by using the Git software with the following commands

* git add *file(s)* name 
* git commit -m "commit description"
* git push

### Heroku
Heroku is used to host the application.  Heroku will need to know what dependencies/applications are needed to run the app.  These should be stored in the requirement.txt file.  

Using pip3 use the following command: pip3 freeze --local > requirements.txt
A Procfile  is also needed so Heroku knows how to run the app.  which an be created with the following command: echo web: python *{name of .py file}* > Procfile.

Then:

1.Go to [Heroku.com](https://www.heroku.com/) and create an account/login.
1. Click create new app, provide a name for your app and select the region near your location.
1. Click create app.
1. There are various methods to deploy the application and you should refer to the Heroku documentation [here](https://devcenter.heroku.com/categories/reference#deployment) if you want further information on all the methods.  I used automatic deployment from GitHub.  To deploy the site in this way click on the deployment tab and then click on the 'GitHub Connect to GitHub' button.  You may then be asked to log in to GitHub at this point.
1. Search for your repository in the 'Search for a repository to connect to' section.
1.  click 'Connect' when you have found your repository.
1. Next click on the 'Settings' tab near the top of the page and go to 'reveal Config Vars'.
1. You will then need to input the variables that you will have stored in your env .py.
1. Next click the 'Deploy' at top near the top of the page and click 'Enable Automatic Deployment'
10.Next click 'Deploy Branch', If there is more than one branch make sure you select the branch you want to deploy. 
1. App will then be built by Heroku and a link to the deployed site will be provided.

Please note, for the application to work as it is coded now, you will need to crate a collection for the database in mongoDB.  The Schema to be used is provided above in this README.


### Cloning The Site

1. From within the repository click on 'Code' button with the download icon.
2. A small menu will appear to give you various options.  One option is to copy the URL provided in this menu.
3. Within the Integrated Development Environment (IDE) that you are using, change the directory to the ULR you have just copied.
4. For more options and details as to how to clone the site click [here](https://docs.github.com/en/free-pro-team@latest/github/using-git/which-remote-url-should-i-use) You may need to be logged into GitHub to view this page.

____

## Credits

### Images

[Hero Image](https://unsplash.com/photos/wMzx2nBdeng) -from Unsplash by Brooke Lark

All recipes are from http://allrecipes.co.uk/ and can be found by searching the name of the recipe in the search function.





## General Credits

**Bootstrap** has been used to create the grid system.  It has also been used to create the navbar, forms and recipe cards and the recipe lists.  However all have been customised by me

**Google Fonts:**  Fonts for this project are from Google Fonts.  The import at the top of the CSS file was copied from Google Fonts.

**Mail Icon:** The icons used in the site are from Font Awesome

**Code Institue** The functions I have built in the app.py file are from my learning in the Code Institute Full Stack Developer Course and influenced from the mini work though project: Task List

## Acknowledgements

Thanks go to:

* My mentor, Brian Macharia for his continued  advice and feedback.

* The Code Institute Slack Community who are always on hand to answer queries.

* The Code Institute Tutors for their assistance with any queries.


