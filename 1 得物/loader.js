
// 将global对象赋值给window变量 打包工具为了兼容不同环境，确保代码在不同环境中都能访问到全局变量
window = global
!function(e) {
    function r(r) {
        for (var n, a, i = r[0], c = r[1], l = r[2], p = 0, s = []; p < i.length; p++)
            a = i[p],
            Object.prototype.hasOwnProperty.call(o, a) && o[a] && s.push(o[a][0]),
            o[a] = 0;
        for (n in c)
            Object.prototype.hasOwnProperty.call(c, n) && (e[n] = c[n]);
        for (f && f(r); s.length; )
            s.shift()();
        return u.push.apply(u, l || []),
        t()
    }
    function t() {
        for (var e, r = 0; r < u.length; r++) {
            for (var t = u[r], n = !0, i = 1; i < t.length; i++) {
                var c = t[i];
                0 !== o[c] && (n = !1)
            }
            n && (u.splice(r--, 1),
            e = a(a.s = t[0]))
        }
        return e
    }
    var n = {}
      , o = {
        0: 0
    }
      , u = [];
    function a(r) {
        if (n[r])
            return n[r].exports;
        var t = n[r] = {
            i: r,
            l: !1,
            exports: {}
        }
          , o = !0;
        try {
            // 这里打印日志 观察缺少哪些模块
            console.log('r:::',r)
            e[r].call(t.exports, t, t.exports, a),
            o = !1
        } finally {
            o && delete n[r]
        }
        return t.l = !0,
        t.exports
    }
    // 这种就是加载器函数 形如x.y = function(){}且获取，处理并提供了代码或模块供程序使用
    // 函数a是webpack打包后的主模块加载函数，它负责根据传入的模块ID(r)来查找执行对应的模块代码 使得每次a(r)被调用时，能看到模块的ID(r)被打印出来

// 将global对象赋值给window变量 打包工具为了兼容不同环境，确保代码在不同环境中都能访问到全局变量
window = global
!function(e) {
    function r(r) {
        for (var n, a, i = r[0], c = r[1], l = r[2], p = 0, s = []; p < i.length; p++)
            a = i[p],
            Object.prototype.hasOwnProperty.call(o, a) && o[a] && s.push(o[a][0]),
            o[a] = 0;
        for (n in c)
            Object.prototype.hasOwnProperty.call(c, n) && (e[n] = c[n]);
        for (f && f(r); s.length; )
            s.shift()();
        return u.push.apply(u, l || []),
        t()
    }
    function t() {
        for (var e, r = 0; r < u.length; r++) {
            for (var t = u[r], n = !0, i = 1; i < t.length; i++) {
                var c = t[i];
                0 !== o[c] && (n = !1)
            }
            n && (u.splice(r--, 1),
            e = a(a.s = t[0]))
        }
        return e
    }
    var n = {}
      , o = {
        0: 0
    }
      , u = [];
    function a(r) {
        if (n[r])
            return n[r].exports;
        var t = n[r] = {
            i: r,
            l: !1,
            exports: {}
        }
          , o = !0;
        try {
            // 这里打印日志 观察缺少哪些模块
            console.log('r:::',r)
            e[r].call(t.exports, t, t.exports, a),
            o = !1
        } finally {
            o && delete n[r]
        }
        return t.l = !0,
        t.exports
    }
    // 这种就是加载器函数 形如x.y = function(){}且获取，处理并提供了代码或模块供程序使用
    // 函数a是webpack打包后的主模块加载函数，它负责根据传入的模块ID(r)来查找执行对应的模块代码 使得每次a(r)被调用时，能看到模块的ID(r)被打印出来
    window.loader = a
    // 将这个核心的模块加载函数暴露到全局作用域下。避免被垃圾回收，使得可以在外部访问 (可以直接在另个要导入到的js文件测试能否打印,测试bug)
    a.e = function(e) {
        var r = []
          , t = o[e];
        if (0 !== t)
            if (t)
                r.push(t[2]);
            else {
                var n = new Promise((function(r, n) {
                    t = o[e] = [r, n]
                }
                ));
                r.push(t[2] = n);
                var u, i = document.createElement("script");
                i.charset = "utf-8",
                i.timeout = 120,
                a.nc && i.setAttribute("nonce", a.nc),
                i.src = function(e) {
                    return a.p + "static/chunks/" + ({}[e] || e) + "." + {
                        31: "ecac32f99e0ca09d21e6",
                        32: "a463ab2b110615917c04"
                    }[e] + ".js"
                }(e);
                var c = new Error;
                u = function(r) {
                    i.onerror = i.onload = null,
                    clearTimeout(l);
                    var t = o[e];
                    if (0 !== t) {
                        if (t) {
                            var n = r && ("load" === r.type ? "missing" : r.type)
                              , u = r && r.target && r.target.src;
                            c.message = "Loading chunk " + e + " failed.\n(" + n + ": " + u + ")",
                            c.name = "ChunkLoadError",
                            c.type = n,
                            c.request = u,
                            t[1](c)
                        }
                        o[e] = void 0
                    }
                }
                ;
                var l = setTimeout((function() {
                    u({
                        type: "timeout",
                        target: i
                    })
                }
                ), 12e4);
                i.onerror = i.onload = u,
                document.head.appendChild(i)
            }
        return Promise.all(r)
    }
    ,
    a.m = e,
    a.c = n,
    a.d = function(e, r, t) {
        a.o(e, r) || Object.defineProperty(e, r, {
            enumerable: !0,
            get: t
        })
    }
    ,
    a.r = function(e) {
        "undefined" !== typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {
            value: "Module"
        }),
        Object.defineProperty(e, "__esModule", {
            value: !0
        })
    }
    ,
    a.t = function(e, r) {
        if (1 & r && (e = a(e)),
        8 & r)
            return e;
        if (4 & r && "object" === typeof e && e && e.__esModule)
            return e;
        var t = Object.create(null);
        if (a.r(t),
        Object.defineProperty(t, "default", {
            enumerable: !0,
            value: e
        }),
        2 & r && "string" != typeof e)
            for (var n in e)
                a.d(t, n, function(r) {
                    return e[r]
                }
                .bind(null, n));
        return t
    }
    ,
    a.n = function(e) {
        var r = e && e.__esModule ? function() {
            return e.default
        }
        : function() {
            return e
        }
        ;
        return a.d(r, "a", r),
        r
    }
    ,
    a.o = function(e, r) {
        return Object.prototype.hasOwnProperty.call(e, r)
    }
    ,
    a.p = "",
    a.oe = function(e) {
        throw console.error(e),
        e
    }
    ;
    var i = window.webpackJsonp_N_E = window.webpackJsonp_N_E || []
      , c = i.push.bind(i);
    i.push = r,
    i = i.slice();
    for (var l = 0; l < i.length; l++)
        r(i[l]);
    var f = c;
    t()
}([]);

    // 将这个核心的模块加载函数暴露到全局作用域下。避免被垃圾回收，使得可以在外部访问 (可以直接在另个要导入到的js文件测试能否打印,测试bug)
    a.e = function(e) {
        var r = []
          , t = o[e];
        if (0 !== t)
            if (t)
                r.push(t[2]);
            else {
                var n = new Promise((function(r, n) {
                    t = o[e] = [r, n]
                }
                ));
                r.push(t[2] = n);
                var u, i = document.createElement("script");
                i.charset = "utf-8",
                i.timeout = 120,
                a.nc && i.setAttribute("nonce", a.nc),
                i.src = function(e) {
                    return a.p + "static/chunks/" + ({}[e] || e) + "." + {
                        31: "ecac32f99e0ca09d21e6",
                        32: "a463ab2b110615917c04"
                    }[e] + ".js"
                }(e);
                var c = new Error;
                u = function(r) {
                    i.onerror = i.onload = null,
                    clearTimeout(l);
                    var t = o[e];
                    if (0 !== t) {
                        if (t) {
                            var n = r && ("load" === r.type ? "missing" : r.type)
                              , u = r && r.target && r.target.src;
                            c.message = "Loading chunk " + e + " failed.\n(" + n + ": " + u + ")",
                            c.name = "ChunkLoadError",
                            c.type = n,
                            c.request = u,
                            t[1](c)
                        }
                        o[e] = void 0
                    }
                }
                ;
                var l = setTimeout((function() {
                    u({
                        type: "timeout",
                        target: i
                    })
                }
                ), 12e4);
                i.onerror = i.onload = u,
                document.head.appendChild(i)
            }
        return Promise.all(r)
    }
    ,
    a.m = e,
    a.c = n,
    a.d = function(e, r, t) {
        a.o(e, r) || Object.defineProperty(e, r, {
            enumerable: !0,
            get: t
        })
    }
    ,
    a.r = function(e) {
        "undefined" !== typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {
            value: "Module"
        }),
        Object.defineProperty(e, "__esModule", {
            value: !0
        })
    }
    ,
    a.t = function(e, r) {
        if (1 & r && (e = a(e)),
        8 & r)
            return e;
        if (4 & r && "object" === typeof e && e && e.__esModule)
            return e;
        var t = Object.create(null);
        if (a.r(t),
        Object.defineProperty(t, "default", {
            enumerable: !0,
            value: e
        }),
        2 & r && "string" != typeof e)
            for (var n in e)
                a.d(t, n, function(r) {
                    return e[r]
                }
                .bind(null, n));
        return t
    }
    ,
    a.n = function(e) {
        var r = e && e.__esModule ? function() {
            return e.default
        }
        : function() {
            return e
        }
        ;
        return a.d(r, "a", r),
        r
    }
    ,
    a.o = function(e, r) {
        return Object.prototype.hasOwnProperty.call(e, r)
    }
    ,
    a.p = "",
    a.oe = function(e) {
        throw console.error(e),
        e
    }
    ;
    var i = window.webpackJsonp_N_E = window.webpackJsonp_N_E || []
      , c = i.push.bind(i);
    i.push = r,
    i = i.slice();
    for (var l = 0; l < i.length; l++)
        r(i[l]);
    var f = c;
    t()
}([]);
