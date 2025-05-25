## 1. 得物 (dewu.com) 签名分析与数据抓取

这个案例主要展示了如何对得物网站的 API 请求签名进行逆向分析，并使用 Python 和 JavaScript 运行时 (`execjs`) 来生成签名，从而成功抓取数据。

**配套代码**
该文章配套图文讲解已发布到[CSDN](https://blog.csdn.net/2401_87328929/article/details/148026298)


**文件说明：**

* `dewu.py`: 主 Python 爬虫脚本，负责发起 HTTP 请求，调用 JS 代码生成签名，并处理响应数据。
* `dewu.js`: 从得物网站提取的 JavaScript 代码片段，包含了用于生成签名或其他关键参数的逻辑。
* `loader.js`: 加载器，用于对webpack相关的代码处理并传递给dewu.js
* `mod01.js`, `mod02.js`:  同loader.js
* `readme.md`: 当前文件，项目说明。

**运行方法：**

1.  确保您安装了 Python 和必要的库：`pip install requests execjs`
2.  确保您的系统中安装了 JavaScript 运行环境，推荐安装 [Node.js](https://nodejs.org/)。
3. 运行主脚本：`python dewu.py`
4. 最终获得sign与对应正确的请求结果

**逆向分析思路：**

* 通过浏览器开发者工具观察网络请求，找到需要签名的 API。
* 在发起请求前的 JS 代码中搜索与 `sign` 相关的关键字。
* 在找到的 JS 代码处设置断点，跟踪签名值的生成过程。
* 定位到实际生成签名的 JS 函数或代码块。
* 提取并整理所需的 JS 代码。
* 使用 `execjs` 在 Python 中执行这部分 JS 代码来生成签名。

**注意事项：**

* 网站的反爬机制可能会更新。
* 抓取网站数据应遵守相关法律法规和网站的使用协议。