// 仅需加密逻辑--webpack
// 没绷住..这个看似加密的o实际上压根就是个不动值..白扣半天
// 以后看到某些像是动值的，你先别急，多测试几遍看动不动，能省非常大的工作量。

//这里w_rid请求返回了两次不同值，第一次简单第二次复杂。只放进第一次的值应该也是可以的
const crypto_js = require('crypto-js')


// w_rid
// e = "7cd084941338484aae1ad9425b84077c4932caff0ff746eab6f01bf08b70ac45"
// wbiImgKey1 = "d569546b86c252:db:9bc7e99c5d71e5"
// wbiSubKey1 = "557251g796:g54:f:ee94g8fg969e2de"
// formatString$1 = function(e) {
//         for (var t = "", r = 0; r < e.length; r++)
//             t += String.fromCharCode(e.charCodeAt(r) - 1);
//         return t
//     }
// t = {
//     "wbiImgKey2":formatString$1(wbiImgKey1),
//     "wbiSubKey2":formatString$1(wbiSubKey1)
// }
// function getLocal(e) {
//         try {
//             return localStorage.getItem(e)
//         } catch (e2) {
//             return null
//         }
//     }
// function getImgFormatConfig(e) {
//         var t;
//         if (e.useAssignKey)
//             return {
//                 imgKey: wbiImgKey2,
//                 subKey: wbiSubKey2
//             };
//         var r = (null === (t = getLocal("wbi_img_urls")) || void 0 === t ? void 0 : t.split("-")) || []
//           , n = r[0]
//           , i = r[1];
//         return {
//             imgKey: n ? getKeyFromURL(n) : e.wbiImgKey,
//             subKey: i ? getKeyFromURL(i) : e.wbiSubKey
//         }
//     }
// r = getImgFormatConfig(t)
// n = r.imgKey
// i = r.subKey
// function getPictureHashKey(e) {
//         var t = [];
//         return [46, 47, 18, 2, 53, 8, 23, 32, 15, 50, 10, 31, 58, 3, 45, 35, 27, 43, 5, 49, 33, 9, 42, 19, 29, 28, 14, 39, 12, 38, 41, 13, 37, 48, 7, 16, 24, 55, 40, 61, 26, 17, 0, 1, 60, 51, 30, 4, 22, 25, 54, 21, 56, 59, 6, 63, 57, 62, 11, 36, 20, 34, 44, 52].forEach((function(r) {
//             e.charAt(r) && t.push(e.charAt(r))
//         }
//         )),
//         t.join("").slice(0, 32)
//     }
// o = getPictureHashKey(n + i)

function get_w_rid(timestamp) {
    o = "ea1db124af3c7062474693fa704f4ff8"
    f = `web_location=333.337&wts=${timestamp}`
    return crypto_js.MD5(f + o).toString()
}


// qv_id
function o5(e) {
    return typeof e == "boolean"
}

function s5(e, t, n) {
    var r = Math.random();
    if (!tr(e))
        return r;
    o5(t) && (n = t);
    var a;
    return !tr(t) || t === e ? a = r * e : a = r * (t - e) + e,
        n ? a : Math.floor(a)
}

function ll(e) {
    return e instanceof Array
}

function i5(e, t) {
    var n = _p(e);
    n && (e = e.split("")),
    ll(e) || (e = []);
    for (var r = e.slice(), a = -1; ++a < r.length;)
        for (var o = a, i = function () {
            var l = r[a]
                , u = r[o]
                , c = ll(t)
                , f = !c && (t ? l == u : l === u) || c && t.some(function (d) {
                return l && u && !hv(l[d]) && l[d] === u[d]
            });
            f && r.splice(o--, 1)
        }; ++o < r.length;)
            i();
    return n ? r.join("") : r
}

var cd = "0123456789"
    , Pp = "abcdefghijklmnopqrstuvwxyz"
    , fd = Pp.toUpperCase()
    , C0 = "~`!@#$%^&*()-_+=[]{};:\"',<.>/?";

function tr(e, t) {
    var n = typeof e == "number";
    return t ? n : n && !Number.isNaN(e) && Number.isFinite(e)
}

function _p(e) {
    return typeof e == "string"
}

function En(e, t) {
    _p(e) && (t = e),
    tr(e) || (e = 12);
    var n = "";
    !t || !_p(t) ? n = cd + fd : t === "[*]" ? n = cd + Pp + fd + C0 : t.match(/0-9|a-z|A-Z|\[s\]/) ? (/0-9/.test(t) && (n += cd),
    /a-z/.test(t) && (n += Pp),
    /A-Z/.test(t) && (n += fd),
    /\[s\]/.test(t) && (n += C0),
        n += i5(t.replace(/0-9|a-z|A-Z|\[s\]/g, ""))) : n = t;
    for (var r = "", a = -1; ++a < e;)
        r += n[s5(n.length)];
    return r
}

a = En(32, "0-9a-zA-Z")


function yt(e) {
    return !!(e && e.__v_isRef === !0)
}

function Ve(e) {
    const t = e && e.__v_raw;
    return t ? Ve(t) : e
}

it = e => e !== null && typeof e == "object"
const Zs = e => it(e) ? Rr(e) : e

function CS(t, n) {
    this.__v_isShallow = n,
        this.dep = void 0,
        this.__v_isRef = !0,
        this._rawValue = n ? t : Ve(t),
        this._value = n ? t : Zs(t)
}

function Mb(e, t) {
    return yt(e) ? e : new CS(e, t)
}

function w(e) {
    return Mb(e, !1)
}

re = w(a)
qv_id = re._value

function get_qv_id() {
    return qv_id
}