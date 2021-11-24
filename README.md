# wiki
This is backend-focused(Django) Wikipedia-like online encyclopedia.

Languages used: Python, HTML5, CSS3
Frameworks used: Django, Bootstrap

It consists: Index page, Entry page, Search, New page, Edit page, Random Page
It takes entries usinf markup language called Markdown.

Entry Page: Visiting /wiki/TITLE, where TITLE is the title of an encyclopedia entry, render a page that displays the contents of that encyclopedia entry.
If an entry is requested that does not exist, it presents user with an error page.

Indes Page: It lists all the entries, from where a user can visit by clicking on entry name.

Search: Allow's the user to type a query into the search box in the sidebar to search for an encyclopedia entry.

New Page: Clicking “Create New Page” in the sidebar take's the user to a page where they can create a new encyclopedia entry. When the page is saved, if an encyclopedia entry already exists with the provided title, the user id presented with an error message.

Edit Page: On each entry page, the user can edit the user Markdown content by clicking edit. The user is serves an error message if it changes the title to a title that already exists.

Random Page: Clicking “Random Page” in the sidebar take's user to a random encyclopedia entry.
