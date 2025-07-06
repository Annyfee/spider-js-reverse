// 主文件 -- 注意填入顺序，env-ts-auto-main尽量以这种格式填入依次加载所需环境

require('./01 env')
require('./02 ts')
require('./03 auto')
// document.cookie即生成最终cookie值，生成正确即可通过瑞数
function get_cookie(){
    return document.cookie
}

// console.log(get_cookie())