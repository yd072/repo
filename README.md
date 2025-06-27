# Custom Cloudflare Speed Test

这是一个使用 [CloudflareSpeedTest](https://github.com/XIU2/CloudflareSpeedTest) 的自动测速项目。

## 使用说明

- 将你想测试的 IP 地址列表写入根目录的 `my_ips.txt` 文件，每行一个 IP。
- GitHub Actions 会自动读取 `my_ips.txt`，使用指定参数跑测速。
- 测速结果会生成 `best_ips.txt`，并自动提交回仓库。
- 你可以在 Actions 页面手动运行，也可以等待每日自动运行。

---

感谢使用！
