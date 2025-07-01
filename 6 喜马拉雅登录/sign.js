cryptoJs = require("crypto-js")

function y(t) {
    var e = ""
        , r = Object.keys(t).sort((function (t, e) {
            return (t = t.charCodeAt(0)) - (e = e.charCodeAt(0))
        }
    ))
        , n = r.length;
    return r.forEach((function (r, o) {
            var i = t[r];
            e += "".concat(r, "=").concat(i),
            o < n - 1 && (e += "&")
        }
    )),
        e
}

function getSignature() {
    var t = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : {}
        , e = y(t) + "&" + "WEB-V1-PRODUCT-E7768904917C4154A925FBE1A3848BC3E84E2C7770744E56AFBC9600C267891F";
    return e.toUpperCase(),
       cryptoJs.SHA1(e.toUpperCase()).toString()
}
