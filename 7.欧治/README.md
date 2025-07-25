### tips
1. 01-05文件为测试cookie的生成逻辑，但全程所用的是静态文件测试。而静态文件的组合生成的cookie2无法通过测试(不信你就去curl to py复制粘贴看能不能出东西)
2. 所以后面的ouyee.js与ouyee.ps俩文件才是最终动态替换的测试成品文件，01-05文件以阅览为主，后者的俩文件才是真正生成对应值的地方。


### 瑞数：
1. 两次请求，一次响应失败一次响应成功。
2. 响应体包含三部分：meta标签(content)+ts代码+一个大自执行函数(auto)--三者合成cookie2 创建格式时，需auto env ts main 四个文件
3. 瑞数五六代返回的都是S(cookie1)/T(cookie2)结尾或O(cookie1)/P(cookie2)结尾的cookie
4. 锁定脚本后再请求就可以看到这个错误返回的具体代码
5. eval在瑞数(auto)里的第二个call里，找到它就是实行入口处，再进去这个call(断点后选择单步调试)，里面的就是真正位置。里面再找undefined即可
6. 做本地替换(仅对meta标签所在的html文件替换即可)：这样瑞数文件的三件套都不会再动态，而是与我的逆向文件同样静态，方便调试
7. 本质上，瑞数就是在补环境时，把原来直观的未定义函数混淆，让我们原本的俩工具（监控器+未定义函）少掉一个，得我们想办法增回去
8. 瑞数只在第一个案例测试时会比较吃力。等你开始做第二个瑞数会发现真的很相似，几乎完全是一套流程和玩法而且里面很多靠经验佐证的东西，别怕。
9. 各种瑞数案例的不同点，主要在补环境的检测点上：它们检测的环境是各有相异的。

### 注意点：
1. 要清cookie，不然202请求获得的c1会存着
2. debugger处理：不用处理，直接按瑞数流程锁定脚本后再请求即可
3. 拿值过来时别用格式化的，不然被瑞数六格式检测就寄
4. 补环境时通常用window=self=top=global
5. VM环境是浏览器生成的代码，专用于在匣子里测试，是一个临时环境
6. 卡住时，window.setInterval=function(){}与window.setTimeout=function(){}的定时器补上，如果还卡就不管接着补
7. 代理监控时，要补的就是属性值为undefined(如果过了可以不用管这，但最后生成仍可能需要) -- 同时一定针对的是get，set不用管
8. 如果补了还没过去，大概率补的这里是有要被用的返回值，需要加个return
9. 补的时候要注意其为方法还是属性，二者补法不一致；一者要写function(){}一者要写{}  不确定就去mdn文档查
10. console.log打印出来的不一定就是返回值，有可能打印的是a，实际返回的是b，只有代码溯源才能确保百分百准确性
11. 瑞数阴就阴在强需求补环境，几乎所有环境都必须要真值，但凡有一两个自己猜的假值都可以报错。这就强制我们必须去溯源代码
12. 处理时，优先消除堵塞与bug，最后再处理假值问题
13. 补环境时，里面所有的混淆代码本质都是对meta标签所在的html文件做操作，多看二者的互动
14. 当方法为set时无需过多关注。重点关注get方法的相关属性
15. 卡在某个对象属性而且你已经为它补过了的话，就为它再打印一次(因为对象属性不一定只会log一次，可能会log多次不同值)
16. 有可能出问题的不是少补，还是多补。某些地方补错了也会使得发现不了错误，补过与没补两种情况都需要考虑
17. 最终调试时，把之前所有console.log与setProxy的打印全部注释掉
18. js与py替换变量或字符串时，严格使用双引号，不然用双引号可能在拼接JS代码块时形成非法语句。eg:a="xx"(js文件) -- y.replace('"xx"',my_def)(py文件)
19. 如果你response返回的是200，但.text无法打印任何东西出来，证明它就是假值!必须回去重新把瑞数挨个补正确，直到打印出东西为止
20. 根据不同的响应结果判断当前处于的不同状态：
    * 跟原url请求一样返回的是三动参：说明cookie生成的不对 -- 大概率环境没补好
    * 404 -- 传入的参数值不够
    * 405 -- 选择的url可能有误
    * 200 -- 打印无东西 - 生成的是假值

### 特征：
1. 多层动态反爬 + js混淆体系(涵盖AST)
2. 处理手法：
   * 补环境(基于proxy代理获得set与get的值)
   * 源码解析(如上，报错时进源码查看)
   * Drissionpage/playwright自动化工具绕过
3. 瑞数整个运行流程：
   * 发起412错误请求，返回源代码，先走content，再给一个ts核心逻辑加密，再走自执行逻辑解密，再用eval(这个eval也被混淆了)
激活vm环境，把源码逻辑解密并返回

### 两条腿走路 
其一为proxy代理调试调试挨个寻找报错位置并补环境
其二为源码解析，报错时进源码查看哪的报错
二者都可以解决问题，结合使用

### 这里给一套瑞数通解流程：
1. 代理监控器+混淆未定义提示，二者都用
2. 优先靠混淆未定义去搜，查看对应代码逻辑。实在太多不好搜再用代理监控器
3. 每个要补的环境都尽可能用console.log打印测试，同时也可以多选择去控制台打印拿值

