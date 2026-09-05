# 📅 历史上的今天

一个基于 GitHub Pages + GitHub Actions 的“历史上的今天”自动更新网站。  
数据来源于「接口盒子」API，每日自动抓取，前端无跨域烦恼，页面优雅简洁。

![网站截图](./screenshot.png)  

🔗 **在线访问**：[https://keaixiaopang.github.io/history-today/](https://keaixiaopang.github.io/history-today/)  

---

## ✨ 特点

- **全自动化**：每天自动调用 API 获取当天历史事件，并更新数据文件。
- **零跨域问题**：前端直接加载同仓库的 `history.json`，无需担心 CORS。
- **响应式设计**：在手机和电脑上都能良好展示。
- **免责声明**：底部包含明确的免责信息，仅供娱乐参考。

---

## 🛠️ 技术栈

- **前端**：纯 HTML + CSS + JavaScript（无第三方依赖）
- **数据源**：[接口盒子](https://www.apihz.cn/) API（免费）
- **自动化**：GitHub Actions（定时任务 + Python 脚本）
- **托管**：GitHub Pages

---

## ⏰ 更新频率

- 默认每天 UTC 18:00（北京时间次日凌晨 2:00）自动更新
- 可在 `.github/workflows/update_history.yml` 中修改 `cron` 表达式

---

## 📝 免责声明

本站“历史上的今天”内容由 **可爱小胖** 使用 **DeepSeek** 辅助编写，数据调用自“接口盒子”API。  
本人不对所展示内容的准确性、完整性和时效性承担任何责任，仅供娱乐参考。

---

## 📄 许可证

[MIT](./LICENSE)

---

**感谢使用！**  
如果你觉得这个项目有用，可以给个 ⭐ 鼓励一下～
