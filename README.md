
# Lootify

[![Build Status](https://travis-ci.org/BrendanMolloy/milestone4.svg?branch=master)](https://travis-ci.org/BrendanMolloy/milestone4)

Lootify is my fourth Milestone Project. <br>
it is an e-commerce website created to display my skills with Full Stack Frameworks.<br>

This website sells props and outfits that cater to Live Action Role Players (LARPers).<br>
LARP is a form of role-playing game where the participants in real life physically portray their characters.<br>
While many players opt to craft their own outfits, some prefer to outright purchase these items, whether due to lack of craft-ability, time, or otherwise.<br>
Lootify offers a wide range of products, which are made easier to browse through by being split into categories.<br>
Whether you're looking for a an impressive set of armor, a convincing-looking prop-sword, or a stylish bag, lootify has it all.

## UX

Lootify was created using the Django, Bootstrap, and Materialize frameworks.<br>
The Superhero theme found at https://bootswatch.com/ was used to create a coherent color scheme. <br>
The Bree Serif font was used to evoke a sense of tradition, history, reliability, 
which speak to the nature of the products and the quality of the service. <br>
Many of the pages found on the website are procedurally generated using the database of products, profiles, and comments.

### User Stories:

* As a LARPer with little crafting skill, I want to purchase some armor, so that I can wear it to an upcoming game.
* As a LARPer who prefers to make their own props, I want to view the weapons sold online, so that I can get some inspiration for a weapon of my own design.
* As a fan of fantasy media, I want to purchase some medieval-themed tchotchkes, so that I can decorate my home with them.

### Wireframes:

![](https://brendans-lootify.s3-eu-west-1.amazonaws.com/media/images/Wireframe+-+Index.png)
##### Index
With Index.html I wanted to create a landing page that would help to orient the user. <br>
The carousel is the feature element of the page, and as such is used to display "featured content". <br>
This code could be modified to instead feature different products, and draw attention to any future sales that may occur.
<br>
I have also included icons for the three categories of products that are sold on the site.<br>
In case the icons themselves are unclear to the user, hovering the cursor over them reveals the category's name.<br>
Clicking on any of these icons will redirect to a pge displaying all products in that category.<br>

![](https://brendans-lootify.s3-eu-west-1.amazonaws.com/media/images/Wireframe+-+All+Products.png)
##### All Products
Using Materialize panels and bootstrap flexbox, 
I've created clean and consistent layout to display the products available on the site.<br>
Clicking on either the product's image or name will direct the user to another page with further detail for that product.<br>
However, they can equally add the desired quantity of that product to their cart from the products page.

![](https://brendans-lootify.s3-eu-west-1.amazonaws.com/media/images/Wireframe+-+Product+detail.png)
##### Product Detail
Again, taking advantage of the bootstrap flexbox, I've created a layout that re-sizes itself to fit different displays.
For viewports of a small size or larger, the product's image takes up a large portion of the screen, 
while the text and form elements accompany it to its side.
The comment section then features at the bottom, 
displaying any comments previously left by other users, ordering them by time and date posted.

## Features

### Existing Features

* Navbar  
    lists links to the home page, the all products, accessories, armor, weapons, and cart pages.
    it also lists context-sensitive links to login, logout, register, or profile pages.
    A searchbar is embedded within the navbar that allows the user to search for specific products by name.
* Carousel
    an interactive display of the featured products, linking to the relevant product pages.
    created using js, the content itself can be modified to instead highlight future sales, or other announcements.
* Profile 
    Users must create an account in order to complete a purchase for any product.
    However, creating an account allows users to update their information to auto-complete the order-form, rather than re-typing their address info for every transaction.
    Being logged in also allows users to post comments to specific product pages.
* Cart 
    By adding quantities of products to the cart, the site can keep track of the products they wish to purchase.
    Users can review their cart to amend quantities of the products they wish to purchase.
* Checkout 
    Displays the cart's contents as a visual confirmation for the user that they are proceeding with the correct purchase.
    Contains two forms, one for shipping details; name, address, etc. and one for the financial transaction, powered using Stripe API
* Orders
    Displays all previous orders made by the user, providing additional confirmation that their order was successful.
    Provides details of the order's date, the product purchased, and the quantity that was purchased.
* Comments 
    Users can leave comments on product pages, such as their reviews or an expression of interest.
    The comment form will only display is user is logged in, but existing comments will display for everyone.
    Similarly, links to edit/delete the comment will only appear if the current user matches the user who left the comment. 
    The edit comment page will display the existing comment as is, and allows the user to update the text.
    The delete page is a confirmation page for the user so that they don't accidentally delete a comment.
* Messages
    Messages will appear near the top of the viewport upon the successful or unssuccesful submission of forms.
* Pagination
    the all_products page lists >10 products, to make content more digestible this is limited to 9 products per page.

### Features Left to Implement

* a change password page. This is presently handled by the editprofile page, but is not the most user-friendly experience, as that page contains two separate forms.
* a sorting function for the products pages (alphabetically, price-ascending, price-descending)
* Contact form
* Email Order Confirmation

### Technologies Used

* [HTML](https://html.com/)  
    Used to put a basic structure on the web pages
* [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)  
    Used to customize formatting and style
* [JS](https://www.javascript.com/)  
    custom javascript was used to create the carousel on index.html
* [Bootstrap](https://getbootstrap.com/)
    For styling, layout
* [Materialize](https://materializecss.com/)  
    For styling purposes, particularly, the panel layouts used for the products
* [Django](https://www.djangoproject.com/)  
    For database management, and page templates
* [Stripe API](https://stripe.com/ie)  
    For handling the financial transactions
* [Python](https://www.python.org/)  
    
## Testing

* Testing was caried out on multiple browsers, includin Chrome, Firefox and Explorer, at multiple resolutions to ensure that formatting remained consistent.
* Travis-CI was used as a continuous integration to perform tests with each git commit
* The Django framework returned error messages whenever there was a conflict in logic
* Used https://validator.w3.org/nu/ to validate HTML and CSS code
* Used http://beautifytools.com/javascript-validator.php to validate JS
* A markdown of test cases can be found [here](https://github.com/BrendanMolloy/milestone4/blob/1c7b984e9ffb72defa1a17b2920f607c87003f97/test_cases.md)


### Known Bugs
* None at present

### Fixed Bugs
* formatting bugs, typically arising due to the inclusion of margin values in custom.css, depsite using bootstrap flexbox
* adding null value quantity of a product to cart now returns a warning mesage to the user.

## Deployment
This project is deployed on Heroku, and can be visited at the following url:  
    https://lootify.herokuapp.com/

To host this project on Heroku, a requirements.txt and Procfile was created, listing required applications for the project.
Config Vars had to uploaded to the Heroku dashboard, including 
AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY_ID, DATABASE_URL, SECRET_KEY, STRIPE_PUBLISHABLE, STRIPE_SECRET.
These allowed the project to access databases from external sources. 
During the development process the values for these variables were held in an env.py file, 
which had been set to be .gitignored and thus kept their sensitive information secret.

A development version of the project was hosted on gitpod. 

Code was regularly committed to github repository to prevent the loss of data.
Following the implementation of covid-19 restrictions I took several weeks off from the course, 
such that when I returned to complete the project, 
the workspace I had been using was deleted from the gitpod servers due to inactivity.
Thanks to my diligent commits to github, the only data lost was the env.py file 
which was easily recreated using the config vars saved to Heroku.

Static files were deployed to a bucket on Amazon Web Service using S3 buckets.

To run the code locally, you will need to generate your own config vars in order to populate the site with products,
and to allow for Stripe functionality.

## Credits
### Media
* The images used for the products on this site were obtained from https://www.medievalcollectibles.com/

### Acknowledgements
Aaron Sinnott, my mentor at Code Institute, for his advice during development

Josh Molloy, my brother, for providing an additional pair of eyes, and assistance in resolving multiple bugs