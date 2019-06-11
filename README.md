### 
###
###
### 如果出现证书错误是因为网站使用的是自签名的证书
    # urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1056)>
    # 解决方案，全局取消证书验证
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context

    
