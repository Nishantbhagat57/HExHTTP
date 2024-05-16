CANARY = "ndvyepenbvtidpvyzh.com"

headersToFuzz = {
    "x-forwarded-scheme": "nohttps",
    "x-forwarded-proto": "nohttps",
    "X_FORWARDED_PROTO": "nohttps",
    "X-Forwarded-Proto-Override": "nohttps",
    "x-forwarded-protocol": "nohttps",
    "x-forward-proto": "nohttps",
    "x-forwarded-proto": "31337",
    "X-Forwarded-Proto-orig": "nohttps",
    "X-Forwarded-Proto-Version": "nohttps",
    "x-wf-forwarded-proto": "foo",
    "X-Forwarded-SSL": "on",
    "X-Forwarded-SSL": "off",
    "X-Url-Scheme": "nohttps",
    "x-http-method-override": "POST",
    "x-http-method-override": "HEAD",
    "x-http-method-override": "PLOP",
    "X-Forwarded-Method": "POST",
    "X-Forwarded-Method": "HEAD",
    "X-Forwarded-Method": "PLOP",
    "x-method-override": "HEAD",
    "X-Forwarded-Port": "31337",
    "X-Forwarded-Timeout": "120",
    "X-Frame-Options": "DENY",
    "X-Forwarded-User": CANARY,
    "x-forwarded-host": CANARY,
    "X-Forwarded-URI": CANARY,
    "x-rewrite-url": CANARY,
    "Orig-path-info": CANARY,
    "X-Forwarded-Access-Token": CANARY,
    "X-Forwarded-Session-ID": CANARY,
    "X-Forwarded-Client-Cert": CANARY,
    "x-host": CANARY,
    "X-Request-Id": CANARY,
    "X-Timer": CANARY,
    "user-agent": CANARY,
    "handle": CANARY,
    "h0st": CANARY,
    "Unencoded-URL": CANARY,
    "x-original-host": CANARY,
    "x-wp-nonce": CANARY,
    "Transfer-Encoding": CANARY,
    "x-original-url": CANARY,
    "Location": CANARY,
    "x-forwarded-prefix": CANARY,
    "x-forwarded-url": CANARY,
    "trailer": CANARY,
    "fastly-ssl": CANARY,
    "fastly-host": CANARY,
    "fastly-ff": CANARY,
    "fastly-client-ip": CANARY,
    "content-type": CANARY,
    "api-version": CANARY,
    "acunetix-header": CANARY,
    "accept-version": CANARY,
    "Access-Control-Allow-Origin": CANARY,
    "Access-Control-Allow-Origin": "*",
    "Base-Url": CANARY,
    "Cache_info": CANARY,
    "Cf-Connecting-Ip": CANARY,
    "Client-IP": CANARY,
    "Coming_from": CANARY,
    "Connect_via_ip": CANARY,
    "Forwarded-For-IP": CANARY,
    "Forwarded-For": CANARY,
    "Forwarded": CANARY,
    "Forwarded_for": CANARY,
    "Forwarded_for_ip": CANARY,
    "Forward-For": CANARY,
    "Forward_for": CANARY,
    "Http-Client-Ip": CANARY,
    "Http-Forwarded-For-Ip": CANARY,
    "Http-Pc-Remote-Addr": CANARY,
    "remote-host-wp": CANARY,
    "remote-host": CANARY,
    "Http-Proxy-Connection": CANARY,
    "Http-Url": CANARY,
    "Http-Via": CANARY,
    "Http-Xroxy-Connection": CANARY,
    "Http-X-Forwarded-For-Ip": CANARY,
    "Http-X-Imforwards": CANARY,
    "Origin": CANARY,
    "Pc_remote_addr": CANARY,
    "Pragma": CANARY,
    "Proxy-Client-Ip": CANARY,
    "Proxy-Host": CANARY,
    "Proxy-Url": CANARY,
    "Proxy-Authorization": CANARY,
    "Proxy": CANARY,
    "Proxy_authorization": CANARY,
    "Proxy_connection": CANARY,
    "Real-Ip": CANARY,
    "Redirect": CANARY,
    "Referer": CANARY,
    "Remote_addr": CANARY,
    "Request-Uri": CANARY,
    "Source-Ip": CANARY,
    "True-Client-Ip": CANARY,
    "Uri": CANARY,
    "Url": CANARY,
    "Via": CANARY,
    "Wl-Proxy-Client-Ip": CANARY,
    "Xonnection": CANARY,
    "Xproxy": CANARY,
    "Xproxy_connection": CANARY,
    "X-Backend-Host": CANARY,
    "X-Bluecoat-Via": CANARY,
    "X-Cache-Info": CANARY,
    "X-Client-IP": CANARY,
    "X-Custom-IP-Authorization": CANARY,
    "X-Forwarded-By": CANARY,
    "X-Forwarded-For-Original": CANARY,
    "X-Forwarded-For": CANARY,
    "Y-Forwarded-For": CANARY,
    "X-Forwarded-Server": CANARY,
    "X-Forwarder-For": CANARY,
    "X-Forward-For": CANARY,
    "X-Forwared-Host": CANARY,
    "X-From-Ip": CANARY,
    "X-From": CANARY,
    "X-Gateway-Host": CANARY,
    "X-Http-Destinationurl": CANARY,
    "X-Http-Host-Override": CANARY,
    "X-Ip": CANARY,
    "X-Originally-Forwarded-For": CANARY,
    "X-Original-Remote-Addr": CANARY,
    "X-Originating-IP": CANARY,
    "X-Proxymesh-Ip": CANARY,
    "X-Proxyuser-Ip": CANARY,
    "X-Proxy-Url": CANARY,
    "X-Real-Ip": CANARY,
    "X-Remote-Addr": CANARY,
    "X-Remote-IP": CANARY,
    "X-Rewrite-Url": CANARY,
    "X-True-IP": CANARY,
    "X_cluster_client_ip": CANARY,
    "X_coming_from": CANARY,
    "X_delegate_remote_host": CANARY,
    "X_forwarded": CANARY,
    "X_forwarded_for_ip": CANARY,
    "X_imforwards": CANARY,
    "X_locking": CANARY,
    "X_looking": CANARY,
    "X_real_ip": CANARY,
    "Zcache_control": CANARY,
    "Z-Forwarded-For": CANARY,
    "x-nextjs-cache": CANARY,
    "X-Echo-Set-Header": CANARY,
    "Cache-Tag": CANARY,
    "IIS-wasurlrewritten": CANARY,
    "Authorization": CANARY,
    "X-CF-APP-INSTANCE": "xxx:1",
    "X-Requested-With": CANARY,
    "X-Content-Type-Options": CANARY,
    "X-Custom-Header": CANARY,
}