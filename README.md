# Profile REST API

- A demo app for using python and Django.
- The app manages user profiles.

# Installation on AWS

1. Setup an Ubuntu tier with a security group that has inbound rule for port 80
2. On server install wget: sudo apt-get install wget
3. Type wget https://raw.githubusercontent.com/baherami/profile-rest-api/master/deploy/server_setup.sh
4. Type chmod +x server_setup.sh
5. Type sudo ./server_setup.sh
6. It will take a while, depending on te server to get ready and at the end there should be a DONE! :) message.
7. Type sudo -i
8. Type source /usr/local/virtualenvs/profiles_api/bin/activate
10. Type python manage.py migrate
11. To create super user type : python manage.py createsuperuser
12. Enter your credentials
13. Type: nano profiles_project/settings.py and add the public DNS of your instance in AWS to the ALLOWED_HOSTS. It should follow this format ALLOWED_HOSTS = ['The Public DNS address']
14. Save the changes in nano and exit nano
15. Type : supervisorctl restart all
16. Server should be up and accessible from browser with the aws public DNS

# Security Notes

This app is just an example of how to develope backends in django. The server API and admin page are not ready for production as they still lack a mechanism for congtroling users registration. A fuzzy script can do unlimited registration to this server.

# Further Developement

This project is just maintained as provided and there is no plan for further developement.
