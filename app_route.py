from flask import Flask, request
# jangan lupa tambahkan request pada import Flask Library
....
VerifyToken='V3rifyT0k3N'
@app.route('/webhook', methods=['GET'])
def webhook():
    if request.method == 'GET':
        if request.args.get("hub.verify_token") == VerifyToken:
            return request.args.get("hub.challenge")
        else:
            return 'Gagal Verifikasi Token'