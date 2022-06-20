# ShareX-ScreenshotServer-Flask
Docker Container.
Provides an Endpoint to upload ShareX screenshots. 
Uses Nginx to host the Screenshots and flask in the backend. 

# Usage in Production
- Create an .env.prod File (see example.env.prod) and set an upload key
- Replace the docker-compose.yml with the production version (docker-compose.prod.yml)
- To use SSL certbot can be integrated.

# ShareX Custom Uploader config example
For more Information see [ShareX Custom Uploader](https://getsharex.com/docs/custom-uploader)
```
{
  "Version": "13.5.0",
  "Name": "ShareXScreenshotServer",
  "DestinationType": "ImageUploader",
  "RequestMethod": "POST",
  "RequestURL": "https://<example.com>/upload",
  "Parameters": {
    "key": "<upload_key>"
  },
  "Body": "MultipartFormData",
  "FileFormName": "image",
  "URL": "$response$",
  "ThumbnailURL": "$response$"
}
```
