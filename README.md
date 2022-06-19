# ShareX-ScreenshotServer-Flask
Docker Container.
Provides an Endpoint to upload ShareX screenshots. 
Uses Nginx to host the Screenshots and flask in the backend. 

# Usage in Production
- Create an .env.prod File (see example.env.prod) and set an upload key
- Replace the docker-compose.yml with the production version (docker-compose.prod.yml)
- To use SSL certbot can be integrated.
