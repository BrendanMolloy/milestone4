# Test Cases

## Nav
#### Searchbar
* Searching for an empty string returns all Products
* Searching for 'a' returns all products with the 'a' character in its name
* Searching for '3' returns no products
* Searchbar still appears in nav when un-collapsed in mobile view
#### Links
* All links found in nav link to the correct page
* All links appear when nav is un-collapsed in mobile view
#### Cart
* Cart shows the correct number of products currently in Cart
* Cart shows the correct number of products when >999 items are currently in cart 
#### Mobile view
* Navbar shows only logo and menu Icons
* Navbar expands to show links and searchbar when menu icon is clicked

## Index
#### Carousel
* Only one slide shows on screen
* Clicking the navigation arrows move the carousel in the indicated direction
* Clicking a navigation dot moves to the associated slide
* Correct navigation dot is highlighted while associated slide is showing
* Slides link to the correct featured products
* Cursor icons changes while hovering over interactable elements, i.e. arrows, slides, dots
#### Category Icons
* Each icon links to the correct page
* Hovering over an icon reveals category name
* Hovering over icon highlights the icon
* Hovering over icon changes cursor

## All Products
#### Links
* Product image and name link to the associated product's page
* Cursor changes when hovering over product image or name
#### Forms
* Adding a quantity of 1 to cart increases the cart integer by 1
* Adding a quantity of 12 to cart increase the cart integer by 12
* Adding a quantity of 0 to cart returns an error message
* Adding a quantity of -452 returns an error message
* Adding a null quantity to cart returns an error message
* Adding a quantity of >999 returns an error message 

## Product Details
#### Form
* Adding a quantity of 2 to cart increases the cart integer by 2
* Adding a quantity of 54 to cart increase the cart integer by 54
* Adding a quantity of 0 to cart returns an error message
* Adding a quantity of -9 returns an error message
* Adding a null quantity to cart returns an error message
* Adding a quantity of >999 returns an error message
#### Comments
* Comment form only appears if logged in
* Previous comments appear whether logged in or navigation
* Comments for other products do not appear
* Submitting a comment refreshes the page with the new comment now present
* 'Edit' and 'Delete' buttons appear beside comments if the current user is the user who submitted the comment
* 'Edit' and 'Delete' buttons do not appear beside comments if the current user is not the user who submitted the comment
* 'Edit' and 'Delete' buttons correctly link to the edit comment and delete comment pages respectively
#### Edit Comment
* Edit comment form displays the original comment
* Submitting the form redirects to the associated product's page, displayinthe newly editted comment
#### Delete Comment
* 'Yes' button deletes the comment and redirects to the associated product's page, now without the deleted comment
* 'Cancel' link redirects to the associated product's page with the comment still intact

## Cart
* Correctly displays all products currently in cart, with correct quantity and total sum of prices.
* Checkout link correctly links to checkout page
#### Form
* Amending a quantity of a product to 3 correctly modifies cart integer and total price
* Amending a quantity of a product to 100 correctly modifies cart integer and total price
* Amending a quantity of a product to 0 correctly modifies cart integer and removes product from cart
* Amending a quantity of a product to -9 returns an error message
* Amending a quantity of a product to a null quantity returns an error message
* Amedning a quantity of a product to >999 returns an error message

## Checkout
* Checkout page correctly renders whether or not user has enterred their profile info
* Correctly displays all products currently in cart, with correct quantity and total sum of prices.
#### Order Form
* Order form fields are pre-populated by user's profile infor if available
* Clicking 'Submit Payment' with properly completed forms successfully creates an order, redirects to index.html, and displays a "Your Order was successful" message
* Trying to submit the form with an empty field will not result in an order being created
* Trying to submit the form with an empty field results in an error message, prompting the user to fill it out and try again
#### Payment Form
* Clicking 'Submit Payment' with properly completed forms successfully creates an order, redirects to index.html, and displays a "Your Order was successful" message
* Trying to submit the form with an empty field will not result in an order being created
* Trying to submit the from with an invalid credit card number will not result in an order being created
* Trying to submit the form with an invalid expiry date will not result in an order being created

## Profile
* Renders whether or not the user has enterred their profile details
* Profile details are coorectly displayed if user has submitted them
* All links direct you to the correct pages
#### Edit Profile
* Fields are pre-populated if user has already submitted their details
* Submitting form with all fields completed updates the user's info, redirects to profile page with form info immediately visible
* Submitting form with an empty field returns an error message, does not update user's profile
#### Email Update
* User's email is pre-populated by email used during registration
* Submitting new email without current password returns an error message, does not update user's email
* Submitting an invalid email address returns an error message, does not update user's email
* Submitting new email with correct password updates the user's email
#### Password Update
* Submitting new password with correct current password and matching fields updates the user's password
* Submitting new password without the correct current password returns an error message, does not update user's password
* Submitting new password that does not match returns an error message, does not update user's password
#### Delete Profile
* 'Yes' button deletes the user's profile and redirects to index.html
* 'Cancel' link redirects to the profile page

## Orders
* Correctly displays the user's previous orders
* Does not display the orders of otehr users

