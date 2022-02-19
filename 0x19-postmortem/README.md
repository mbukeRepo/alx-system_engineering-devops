## Postmortem

Upon testing  frontend application approximately 00:07 Pacific Standard Time (PST),
an issue occured when making an https request to our backend api. A GET request to the api led to ** net::ERR_SSL_PROTOCOL_ERROR **, when the expected response was a JSON string.

### Debugging Process

1. Checked if the https connection is established when requesting our api
`curl api.mbukerepo.tech`

2. Looked in our app.js file if the app was running an https server, and I
found it was running a simple http server (`app.listen(3000)` )

3. imported a https module and created app using createServer method of https
module and then passed the key and certificate generated using ** certbot **
`https.createServer({key, cert},app).listen(3000)`

4. Tested with `curl https://api.mbukerepo.tech` on server, and got response.

### summation

Our frontend app was not establishing a https request because the app was 
running on http.

### Prevention

To avoid this error in the future we are going to make certbot to generate certificates
automatically using `crontab`:

1. open clontab file by `crontab -e`
2. Add the certbot command to run daily. In this example, we run the command every day at noon. The command checks to see if the certificate on the server will expire within the next 30 days, and renews it if so. The --quiet directive tells certbot not to generate output.

```
0 12 * * * /usr/bin/certbot renew --quiet
```
