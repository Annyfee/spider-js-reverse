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
//
// // 如果是普通函数 无需webpack，直接把其not defined的函数扣过来就行   而这里u=r.n(a)明显没那么简单 是个参数传递给函数的属性  而这引入了对象的概念，难度升高(设计初始化 原型模板)
// // 当看到 形如这种结构时： r("ODXe"),r("aCH8"))   就代表了webpack 同时也指加载器调用
// // -- 因为这种 函数名("字符串ID") 的调用模式是 模块打包工具生成的运行时代码 的典型特征  即表明代码是模块化并经过打包的
// // 逗号运算符 形如a = (r("cnSC"),r("ODXe"),r("aCH8"))  的结构 最终返回的是最后一个
// // 使用webpack方式:
// // 1.定位入口确认使用webpack
// // 2. 断点(形如r('xxx')的位置)使用加载器(一般是刷新页面，因为加载器是页面初始化时候加载的)
// // 3. 注意是单文件的还是多文件的webpack(自执行函数里把模块全部加载的是单 放在其他页面再加载的是多) -- 但也要注意，里面加载了也不一定是单(可能不够使用) 但里面为空的一定是多
// // 4. 将加载器文件拷贝到本地 接着做仨事:全局化+日志+观察初始化 (在加日志的情况下运行，如果运行有打印就有初始化，初始化一定要注掉，影响处理精力)
// // 5. 测试加载器的调用，根据模块日志补充mod
