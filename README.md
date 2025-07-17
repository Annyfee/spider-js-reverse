# 🕸️ Spider Js Reverse

> 爬虫 JavaScript 逆向与反调试案例库 | A collection of JS reverse engineering and anti-debugging cases



本仓库聚焦于 JavaScript 逆向分析与前端反爬机制的研究与实战。通过拆解各类网站中的 JS
加密、混淆、环境检测与反调试逻辑，系统记录绕过策略与技术实现，帮助开发者掌握前端反爬常见应对方式。

🔨 本仓库所有案例均配备了README文档，一些难度较大的案例会附上更为详细的README，强烈建议分析源码时附带着使用。

💡 本项目将长期更新，目标是构建一个系统、实用的 JS 逆向分析案例库。

📌 如果你也在研究前端反爬、JavaScript 加密或逆向分析，希望这个项目能为你带来启发和帮助。欢迎 Star、收藏和分享，一起积累、一起进步。

📚 博客同步发布：

👉 [我的CSDN主页](https://blog.csdn.net/2401_87328929)

👉 [CSDN对应专栏](https://blog.csdn.net/2401_87328929/category_12970267.html)

## 🚅 目录跳转

| 站点                                                      | 仓库                                                                                                                                          | 加密算法 | 知识点             | 难度   |
|:--------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------|:-----|:----------------|:-----|
| [得物](https://www.dewu.com/)                             | [🏠](https://github.com/Annyfee/spider-js-reverse/tree/master/1%20%E5%BE%97%E7%89%A9)                                                       | md5  | webpack、扣JS     | ⭐⭐⭐  |
| [微信公众号](https://mp.weixin.qq.com/)                      | [🏠](https://github.com/Annyfee/spider-js-reverse/tree/master/2%20%E5%BE%AE%E4%BF%A1%E5%85%AC%E4%BC%97%E5%8F%B7)                            | md5  | 扣JS、密码学         | ⭐    |
| [福建电子交易平台](https://ggzyfw.fujian.gov.cn/business/list/) | [🏠](https://github.com/Annyfee/spider-js-reverse/tree/master/3%20%E7%A6%8F%E5%BB%BA%E7%94%B5%E5%AD%90%E4%BA%A4%E6%98%93%E5%B9%B3%E5%8F%B0) | AES  | PY算法复现、扣JS、密码学  | ⭐⭐   |
| [烯牛数据](https://www.xiniudata.com/industry/newest)       | [🏠](https://github.com/Annyfee/spider-js-reverse/tree/master/4%20%E7%83%AF%E7%89%9B%E6%95%B0%E6%8D%AE)                                     | md5  | 扣JS             | ⭐⭐   |
| [B站](https://search.bilibili.com/all)                   | [🏠](https://github.com/Annyfee/spider-js-reverse/tree/master/5%20B%E7%AB%99)                                                               | md5  | 扣JS             | ⭐⭐   |
| [喜马拉雅登录](https://passport.ximalaya.com/page/web/login)  | [🏠](https://github.com/Annyfee/spider-js-reverse/tree/master/2%20%E5%BE%AE%E4%BF%A1%E5%85%AC%E4%BC%97%E5%8F%B7%E7%99%BB%E5%BD%95)                   | sha1 | webpack，扣JS，补环境 | ⭐⭐⭐⭐ |
| [欧治钢铁](https://www.ouyeel.com/steel/search)             | [🏠](https://github.com/Annyfee/spider-js-reverse/tree/master/7%20%E6%AC%A7%E6%B2%BB)                   | 无    | 瑞数，补环境          | ⭐⭐⭐⭐⭐ |

## ✨ 适合人群

- 希望系统学习 JavaScript 逆向分析的爬虫工程师。
- 在爬取过程中频繁遇到 JS 反爬障碍的开发者。
- 对前端加密、混淆、反调试技术感兴趣的技术人员。

## 📌 相关项目推荐

- [spider-notebook](https://github.com/Annyfee/spider-notebook)：爬虫基础知识和各类技术笔记库。
- [spider-defense-bypass](https://github.com/Annyfee/spider-defense-bypass)：专注于验证码、滑块、IP 限制等特定反爬技术的突破。

## 🧭 更新计划

本仓库将持续更新 JS 逆向案例，目标为每周或每两周新增一例，在案例增加时会附上全面详尽的README文档。

## ⭐️ 支持与反馈

如果你觉得这个项目对你有帮助，欢迎 Star、Fork、分享给更多人！

若有任何建议或问题，或有想一起研究的 JS 逆向案例，欢迎通过 [Issue](https://github.com/Annyfee/js-spider-reverse/issues)
提出交流！

## ❗ 免责声明

⚠️ 本项目仅用于技术研究与学习，爬取目标均为公开页面内容，并未涉及用户隐私及登录数据。

⚠️ 所有代码请勿用于商业用途，亦不得用于违反目标网站条款的行为。

⚠️ 如目标站方认为涉及侵权，请联系我进行删除与下架处理。