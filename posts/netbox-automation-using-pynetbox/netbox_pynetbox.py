import pynetbox

# Key variables needed to start

NETBOX_URL = 'http://localhost:8000'
TOKEN = '0123456789abcdef0123456789abcdef01234567'

# threading=True

# Instantiate the API object - everything starts from here
nb = pynetbox.api(url=NETBOX_URL, token=TOKEN, threading=True)

print (type(nb))
# Then let's start with the dcim attribute to extract the current vendors list
# As you may have guessed by now, we need to use the API documentation to find the correct URL: pynetbox uses dots
# instead of backslash - /dcim/manufacturers which in pynetbox syntax means:
print(
#list(nb.dcim.manufacturers.all())
nb.dcim.manufacturers.choices()

)


# That cover most of the stuff we want to do, if there is a specific API call you want to make that doesn't fall
# under the above categories, you'll have to interact with the API directing as discussed here.

