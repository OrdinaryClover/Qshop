##支付宝支付demo
from alipay import AliPay
app_public_key_string ="""-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAnU3NoYc29srk32gPmDsT4RAC7h2p9mMYMvxnS3mk2Gl718ZHVwYySL6AdXS9PN800/3KpgwZne+8PBVFFWkOrS//cSR/dFVnHXXQq/Tc4z4YxviMRubKBsxCTNJh+RZFK1u9OuunjNXKZJ/yYd7pt6xcT5TrSrvWiBNhHCUI1coxjno3sItMtTPPlwlYJh2tXOwd4MliMPNjTEUklIR24430EBC16kpNsXTqY227nAraEXyiG+m3AFu+GSFZmdqI7/zDcsQ62FgUTAZDn3I+CU4eiS1IeKr3U2muwqLVQPSzXxh72iMtiDvVnjoD4HacqYpnDOTtQABj9zQOWRwrkQIDAQAB
-----END PUBLIC KEY-----"""
app_private_key_string ="""-----BEGIN PRIVATE KEY-----
MIIEpAIBAAKCAQEAnU3NoYc29srk32gPmDsT4RAC7h2p9mMYMvxnS3mk2Gl718ZHVwYySL6AdXS9PN800/3KpgwZne+8PBVFFWkOrS//cSR/dFVnHXXQq/Tc4z4YxviMRubKBsxCTNJh+RZFK1u9OuunjNXKZJ/yYd7pt6xcT5TrSrvWiBNhHCUI1coxjno3sItMtTPPlwlYJh2tXOwd4MliMPNjTEUklIR24430EBC16kpNsXTqY227nAraEXyiG+m3AFu+GSFZmdqI7/zDcsQ62FgUTAZDn3I+CU4eiS1IeKr3U2muwqLVQPSzXxh72iMtiDvVnjoD4HacqYpnDOTtQABj9zQOWRwrkQIDAQABAoIBAQCHPuysk4/rUnjDqDm4PhsSZ2zNg82s3Hhi5eZ92wGjW9Yxp/WQWfCD4N6bnhpSKurF1bAVYdPomcVytyrlhKUsvFbY1XOL9x2oE7KtFeOQscQl1m7tSuKqQ5ZBbKT1v3MLG14wOYqeKPZR279O7JRv6g6YEcbXQ3bpGhhlVWYqQMmB7cke+JqNslwkNDo4x2OVXYWiBkubiuYT1RLSKLj/TNPbxdRFo2ZpOYbzOLlSuu556VOz+NOcPq+t5u+hYSf+612ko3BXN7N01O6psWKoHowMt3gaRbFFQudnOJXGU5aqCKtJtnzzrzfLrSABRz1kRfopE5jUcCU+VtMK6hwBAoGBAN/yPd9Rr+nLfi/QqngXhSDDiW3OtNgdlP0QitUEihKqOskdFpog826t+AilxMF1u1B6svFXjaRG0pmzaLcJAxEmNfcKhRmBF1+VdurK0/Jf4yqpJ/ag86Fmbm1RXbsZg13VCyGLj1LkEOMqCM//Huh5HLQmzij0TnhgSz0LRYNRAoGBALPRrUzG9n5k0tVliJXJvWFB5lH0RH/2iz0ZhnpmYJwmzFYTYrZ10AyX7joG5i+tLTwaqXGuqcGIElvKdN12oMBk2b70XYwtcytoiVfUA4zKumjDZ6VnXKLAsoYau/RMxe4TssNODAjKhXXp/+1/nsH2SVnDlXcut9UgFZODG5RBAoGAahqxG/ztFx2WJPt9uTaTmelrVL6KSpcBf0F2NeVXse47ugvxKIeSLw94JEi+R1cLr97ip5xu/LWdlLs/UvGPJXHwQaMXWvUh6OS9GhONhhnOXOkWiTDLHd6VVXAms74r0qpdAsDH4GM0aR0CXeInd8fiRKzaIudVwo0FON/9SHECgYEAqh6qp8JsHTPhywXd7GgKBONFtS81RyLGpC1r7ozAxbpnAuAgOaLIC8IJHVi9mUlrTDulJuopq/DB/ZlSatr6RkqjPmcNwbqWBPFHTpJEMYTySn7jpbZeC5Pm0bylKQEhGJYGP4OtGvwOu3mAKP7eAX6x8nx5AWJvhPBvuTkGdIECgYA/Py2NyOIgg9pHkWPIcz3+jFYHjDjpMFZr7vCw0rSNC1AjDid0nR/7CKDN/yQLllXGjrLKk1yLGNuV0T1AoE7QNsKN6onp5cfS28wWgefZW83cbzXxZDry9I5sSMyRUZZLuoo+DToER6uthEZKYiQ9l5MrLZmtaLXW+RrfWuGXmA==
-----END PRIVATE KEY-----"""


##创建实例对象
alipay =AliPay(
    appid = "2016101900723700",
    app_notify_url = None,
    app_private_key_string=app_private_key_string,
    alipay_public_key_string=app_public_key_string,
    sign_type="RSA2",
    debug=False
)

##实例一个订单
order_string = alipay.api_alipay_trade_page_pay(
    subject = "网课服务",  ##主题
    out_trade_no = "23479528757943", ##订单号
    total_amount = "500",  ##交易金额  字符串
    return_url=None,   ##回调的地址
    notify_url=None,   ##通知
)

##返回支付宝支付的url

result = "https://openapi.alipaydev.com/gateway.do?"  + order_string
print(result)