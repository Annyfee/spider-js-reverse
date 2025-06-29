window = global;

window = {
    addEventListener:function (){},
    document:function (){},
    Date:{
        now:function (){}
    },
    requestAnimationFrame:function (){},
    cancelAnimationFrame:function (){}
}

location = {
    "ancestorOrigins": {},
    "href": "https://passport.ximalaya.com/page/web/login?fromUri=https%3A%2F%2Fstudio.ximalaya.com",
    "origin": "https://passport.ximalaya.com",
    "protocol": "https:",
    "host": "passport.ximalaya.com",
    "hostname": "passport.ximalaya.com",
    "port": "",
    "pathname": "/page/web/login",
    "search": "?fromUri=https%3A%2F%2Fstudio.ximalaya.com",
    "hash": ""
}

navigator = {
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'
}

canvas = {
    toDataURL: function (res) {
        // console.log('创建的标签名3:',res)
        return ''
    }
}

document = {
    createElement: function (res) {
        // console.log('创建的标签名1：',res)
        if (res === 'canvas') {
            return canvas
        }
    },
    addEventListener: function () {
    }, // 监听事件本身就没什么返回值
    documentElement: {
        style: {
            fontSize: ''
        }
    },
    getElementById:function (){},
    body:{
        style:{
            fontSize: ''
        }
    }
}


function setProxy(proxyObjArr) {
    for (let i = 0; i < proxyObjArr.length; i++) {
        const handler = `{
      get: function(target, property, receiver) {
        console.log("方法:", "get  ", "对象:", "${proxyObjArr[i]}", "  属性:", property, "  属性类型：", typeof property, ", 属性值：", target[property], ", 属性值类型：", typeof target[property]);
        return target[property];
      },
      set: function(target, property, value, receiver) {
        console.log("方法:", "set  ", "对象:", "${proxyObjArr[i]}", "  属性:", property, "  属性类型：", typeof property, ", 属性值：", value, ", 属性值类型：", typeof target[property]);
        return Reflect.set(...arguments);
      }
    }`;
        eval(`try {
            ${proxyObjArr[i]};
            ${proxyObjArr[i]} = new Proxy(${proxyObjArr[i]}, ${handler});
        } catch (e) {
            ${proxyObjArr[i]} = {};
            ${proxyObjArr[i]} = new Proxy(${proxyObjArr[i]}, ${handler});
        }`);
    }
}


// setProxy(['window', 'document', 'canvas', 'navigator'])
// 环境检测在用subprocess时就可以注释掉了，毕竟这东西会显示的
