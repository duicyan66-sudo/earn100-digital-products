# AI 资料包 GitHub Pages 销售页

这是一个可直接部署到 GitHub Pages 的静态销售页。

## 文件

- `index.html`：销售落地页
- `style.css`：页面样式
- `assets/payment-qr.jpg`：收款二维码
- `samples/free-sample.md`：免费样例
- `downloads/*_paid_encrypted.zip`：加密交付包

## 重要

解压密码没有放在仓库里，保存在本机：

`/root/earn100_github_pages_PASSWORDS_PRIVATE.txt`

不要把这个文件上传到 GitHub。

## GitHub Pages 部署

如果已经有 GitHub 权限：

```bash
cd /root/earn100-github-pages
git init
git add .
git commit -m "Launch digital product landing page"
gh repo create earn100-digital-products --public --source . --push
# GitHub 仓库设置 Pages：Deploy from branch / main / root
```

当前环境没有检测到 GitHub 登录，所以我已经先把网站文件完整生成在本地。
