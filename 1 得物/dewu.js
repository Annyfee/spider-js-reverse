require('./loader')
require('./mod01')
require('./mod02')

// console.log(window.loader)
// window.loader("aCH8")

a = (window.loader("cnSC"),
    window.loader("ODXe"),
    window.loader("aCH8"))

window.loader.n = function (e) {
    var r = e && e.__esModule ? function () {
                return e.default
            }
            : function () {
                return e
            }
    ;
    return window.loader.d(r, "a", r),
        r
}
u = window.loader.n(a)

// console.log(u)
function c(t) {
    return u()("".concat(t ? Object.keys(t).sort().reduce((function (e, r) {
            var n = t[r];
            if (void 0 === n)
                return e;
            if (Number.isNaN(n) && (n = ""),
                Array.isArray(n)) {
                if (0 === n.length)
                    return "".concat(e).concat(r);
                var o = n.sort().map((function (t) {
                        return t instanceof Object ? JSON.stringify(t) : t
                    }
                )).reduce((function () {
                        var t = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : ""
                            , e = arguments.length > 1 ? arguments[1] : void 0;
                        return t + (t ? "," : "") + e
                    }
                ));
                return "".concat(e).concat(r).concat(o)
            }
            return n instanceof Object ? e + r + JSON.stringify(n) : e + r + n.toString()
        }
    ), "") : "", "048a9c4943398714b356a696503d2d36"))
}

let data = {
    "pickRuleId": 644479,
    "pageNum": 1,
    "pageSize": 24,
    "filterUnbid": true,
    "showCspu": true
}

// c(data)
// console.log(c(data))


