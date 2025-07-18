// 环境
// content文件
// content = "6PWkevrej8oSnK4bjyH2EMA_i5umaKsc0Sa6NV1SfyIE1UwCEMYpM1aBNeKwKcTsh6QRiTukdOf4rLoCVWcNUqJTc.xvRzbvby830fRjYfEIhLN6Nyg.miFNFKFKiDcKDxSuJjYLz7QfUYR2_1gnD.v1blOGu6g1pqUSmeGOBhVwbFnv1KeC5Id_4zqdwhBcQGrPgmIvkyMEaedN3MoeTtLJMK8x_DpsUFePRhKOsSa"
content = 'metaContent'
// 放置环境与proxy检测的地儿

window = self = top = global;

// window.parseFloat = {}
// window.webkitRequestFileSystem = {} // 不要瞎补这些多出来看似有用实则完全无用纯干扰人的东西
window.addEventListener = function (){}
window.setInterval = function () {}
window.setTimeout = function () {}
window.ActiveXObject = undefined

location = {
    "ancestorOrigins": {},
    "href": "https://www.ouyeel.com/steel/search?keySearch=&pageIndex=0&pageSize=50",
    "origin": "https://www.ouyeel.com",
    "protocol": "https:",
    "host": "www.ouyeel.com",
    "hostname": "www.ouyeel.com",
    "port": "",
    "pathname": "/steel/search",
    "search": "?keySearch=&pageIndex=0&pageSize=50",
    "hash": ""
}

navigator = {
    userAgent:'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 '
}

i = {}

div = {
    getElementsByTagName(ele) {
        // console.log('div getElementsByTagName',ele)
        if (ele === 'i') {
            return []
        } else{
            return []
        }
    }
}

head = {
    removeChild() {

    }
}

script = {
    getAttribute(ele) {
        // console.log('script getAttribute',ele)
        if (ele === 'r') {
            return 'm'
        }
    },
    parentElement: head,
}
meta = {
        getAttribute(ele) {
        // console.log('meta getAttribute',ele)
        if (ele === 'r') {
            return 'm'
        }
    },
    parentNode:head,
    content:content
}

form = {}

document = {
    createElement(ele) {
        console.log('document createElement',ele)
        if (ele === 'div') {
            return div
        } else if (ele === "form") {
            return form
        } else {
            return {} // 当有其他情况时，让其返回空数组而非undefined
        }
    },
    appendChild(ele) {
        // console.log('document appendChild',ele)
        return {}
    },
    removeChild(ele) {
        // console.log('document removeChild',ele)
        return {}
    },
    getElementsByTagName(ele) {
        // console.log('document getElementsByTagName',ele)
        if (ele === 'script') {
            return [script, script]
        }else if(ele==='meta'){
            return [meta,meta]
        }else if(ele==='base'){
            return []
        }else{
            return []
        }
    },
    getElementById() {
        // console.log('document getElementById',ele)
        // 不重要的值
    }
}



// 源码

"ts_js"
;
"auto_js"
;


// api
function get_cookie(){
    return document.cookie
}

// console.log(get_cookie())
