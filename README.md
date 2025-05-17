# 🕸️ Spider Js Reverse Cases

> 爬虫 JavaScript 逆向与反调试案例库 | A collection of JS reverse engineering and anti-debugging cases

本仓库专注于 JavaScript 逆向分析与反调试技术的学习和实战。通过对各种网站的 JS 加密、混淆、反调试、环境检测等手段进行**案例拆解和详细记录**，旨在帮助开发者掌握绕过前端反爬的常用技巧。

📚 博客同步发布：

👉 [我的CSDN主页](https://blog.csdn.net/2401_87328929)

## 📖 仓库结构

```
spider-js-reverse/
├── cases/                 # 案例分析代码和笔记
│   ├── case_01_websiteA/  # 案例1：网站A
│   │   ├── README.md      # 案例说明和分析过程
│   │   ├── demo.py        # Python 演示代码
│   │   └── js/            # 提取或还原的 JS 代码
│   │       └── ...
│   ├── case_02_websiteB/  # 案例2：网站B
│   │   └── ...
│   └── ...
├── utils/                 # 可能用到的工具函数与脚本
├── README.md              # 项目说明
└── .gitignore             # Git 忽略文件
```

## 📌 内容主题（持续更新中）

- **网站 JS 签名算法逆向：** 对 API 请求中 `sign`、`_signature`、`tk` 等参数的生成进行分析和还原。
- **JS 代码混淆与加密还原：** 针对 Webpack、各种混淆工具（如 Obfuscator）处理后的代码进行去混淆和结构分析。
- **反调试技术对抗：** 浏览器 debugger 检测、`debugger` 语句、控制台检测等绕过方法。
- **浏览器环境检测绕过：** 对 `window`、`navigator`、`puppeteer` 等浏览器环境特征的检测和伪造。
- **Canvas、字体、CSS 偏移等渲染反爬分析。**
- **动态代码加载与执行分析：** 异步加载模块、`eval`、`Function` 构造函数等。
- **常用工具使用：** 浏览器开发者工具、抓包工具（Charles, Fiddler, Wireshark）、Node.js 执行环境、`execjs`、`frida` 等。

每篇案例力求从实战网站出发，详细记录分析思路、调试过程和最终的代码实现。

## ✨ 适合人群

- 希望系统学习 JavaScript 逆向分析的爬虫工程师。
- 在爬取过程中频繁遇到 JS 反爬障碍的开发者。
- 对前端加密、混淆、反调试技术感兴趣的技术人员。

## 📌 相关项目推荐

- [spider-notebook](https://github.com/Annyfee/spider-notebook)：爬虫基础知识和各类技术笔记库。
- [spider-defense-bypass](https://github.com/Annyfee/spider-defense-bypass)：专注于验证码、滑块、IP 限制等特定反爬技术的突破。

## 🧭 更新计划

本仓库计划持续更新 JS 逆向案例，力争每周或每半月贡献新的案例分析。

## ⭐️ 支持与反馈

如果你觉得这个项目对你有帮助，欢迎 Star、Fork、分享给更多人！

若有任何建议或问题，或有想一起研究的 JS 逆向案例，欢迎通过 [Issue](https://github.com/Annyfee/js-spider-reverse/issues) 提出交流！