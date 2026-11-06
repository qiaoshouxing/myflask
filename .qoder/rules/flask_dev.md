---
trigger: always_on
---

# Flask 男士假发展示网站开发规范

## 项目概述

本项目是一个基于 Python Flask 框架开发的静态商品展示网站，主要展示男士假发产品。网站采用前后端分离的设计理念，后端使用 Flask 提供路由和模板渲染服务，前端使用 HTML、CSS、JavaScript 构建用户界面。

## 技术栈规范

### 后端技术栈
- **框架**: Flask (最新稳定版)
- **Python 版本**: Python 3.8+
- **模板引擎**: Jinja2 (Flask 内置)
- **配置管理**: 使用 config.py 进行配置管理

### 前端技术栈
- **HTML5**: 语义化标签
- **CSS3**: 响应式设计，支持移动端适配
- **JavaScript**: 原生 JS + jQuery (如需要)
- **图标库**: Remix Icon
- **字体**: 自定义字体 (HolligateSignatureDemo 等)

## 项目结构规范

```
myflask/
├── manhair/                    # 男士假发产品模块
│   ├── assets/                 # 静态资源目录
│   │   ├── css/               # 样式文件
│   │   │   ├── style.css     # 主样式文件
│   │   │   ├── theme.css     # 主题样式
│   │   │   ├── plugin.css    # 插件样式
│   │   │   └── collection.css # 集合页样式
│   │   ├── js/                # JavaScript 文件
│   │   │   ├── theme.js      # 主题脚本
│   │   │   └── plugin.js     # 插件脚本
│   │   ├── font/              # 字体文件
│   │   └── image/             # 图片资源
│   │       ├── product/       # 产品图片
│   │       ├── banner-*.jpg   # 横幅图片
│   │       └── slider-*.jpg   # 轮播图片
│   ├── templates/             # HTML 模板
│   │   ├── index.html        # 首页模板
│   │   └── products_macro.html # 产品宏文件
│   └── __init__.py           # 模块初始化
├── config.py                  # 配置文件
└── .venv/                     # 虚拟环境
```

## Flask 开发规范

### 1. 应用初始化

```python
# manhair/__init__.py
from flask import Flask

def create_app(config_name=None):
    app = Flask(__name__)
    
    # 加载配置
    if config_name:
        app.config.from_object(config[config_name])
    else:
        app.config.from_object(config['default'])
    
    # 注册蓝图
    from .routes import main
    app.register_blueprint(main)
    
    return app
```

### 2. 路由规范

- 使用蓝图 (Blueprint) 组织路由
- 路由命名采用 snake_case
- 产品相关路由使用 `/products` 前缀
- 静态页面直接使用模板渲染

```python
from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    """首页"""
    return render_template('index.html')

@main.route('/products')
def products():
    """产品列表页"""
    return render_template('products.html')

@main.route('/products/<product_id>')
def product_detail(product_id):
    """产品详情页"""
    return render_template('product_detail.html', product_id=product_id)
```

### 3. 模板开发规范

- 使用 Jinja2 模板继承机制
- 公共部分提取为宏 (macro) 或包含文件
- 产品卡片、导航栏等重复组件使用宏定义
- 模板文件使用 `.html` 扩展名

```html
<!-- 使用宏定义产品卡片 -->
{% macro product_card(product) %}
<div class="product-card">
    <img src="{{ product.image }}" alt="{{ product.name }}">
    <h3>{{ product.name }}</h3>
    <p class="price">¥{{ product.price }}</p>
</div>
{% endmacro %}
```

### 4. 静态资源管理

- 所有静态资源放在 `assets/` 目录下
- 使用 `url_for('static', filename='...')` 生成静态文件 URL
- CSS 文件按功能分离，避免单个文件过大
- JavaScript 采用渐进增强，确保核心功能可用

### 5. 配置管理

```python
# config.py
class Config:
    """基础配置"""
    SECRET_KEY = 'your-secret-key'
    DEBUG = False

class DevelopmentConfig(Config):
    """开发环境配置"""
    DEBUG = True

class ProductionConfig(Config):
    """生产环境配置"""
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
```

## 男士假发产品展示规范

### 1. 产品分类

男士假发产品按以下维度分类：
- **材质**: 真人发、合成纤维、混合材质
- **款式**: 全头套、半头套、补发块
- **颜色**: 黑色、棕色、金色、灰色等
- **长度**: 短发、中发、长发

### 2. 产品信息结构

每个产品应包含以下信息：
```python
product = {
    'id': 'unique_id',
    'name': '产品名称',
    'category': '分类',
    'material': '材质',
    'color': '颜色',
    'length': '长度',
    'price': 0.00,
    'description': '产品描述',
    'images': ['image1.jpg', 'image2.jpg'],
    'features': ['特点1', '特点2'],
    'in_stock': True
}
```

### 3. 图片规范

- 产品图片统一尺寸，建议 800x800px
- 支持多角度展示（正面、侧面、背面）
- 使用 WebP 格式优化加载速度
- 图片命名规范：`product-{id}-{angle}.jpg`

### 4. 页面设计要点

- **首页**: 突出主打产品，展示品牌特色
- **产品列表**: 支持筛选、排序、分页
- **产品详情**: 大图展示、详细信息、购买按钮
- **响应式**: 移动端优先，适配各种屏幕尺寸

## 代码风格规范

### Python 代码规范

- 遵循 PEP 8 编码规范
- 使用 4 个空格缩进
- 函数和类添加文档字符串
- 变量和函数名使用 snake_case
- 类名使用 PascalCase
- 常量使用 UPPER_SNAKE_CASE

### 前端代码规范

- HTML 使用语义化标签
- CSS 类名使用 BEM 命名规范（block__element--modifier）
- JavaScript 使用 ES6+ 语法
- 保持代码格式统一，使用编辑配置

## 性能优化规范

### 1. 图片优化
- 使用懒加载 (lazy loading)
- 实现图片压缩和格式优化
- 使用 CDN 加速静态资源

### 2. 缓存策略
- 配置浏览器缓存头
- 使用 Flask-Caching 缓存动态内容
- 实现静态资源版本控制

### 3. 代码优化
- CSS/JS 文件压缩合并
- 减少 HTTP 请求
- 使用异步加载非关键资源

## 安全规范

- 启用 HTTPS
- 配置 CORS 策略
- 防止 XSS 攻击（使用 Jinja2 自动转义）
- 防止 CSRF 攻击（使用 Flask-WTF）
- 定期更新依赖包
- 不在代码中硬编码敏感信息

## 测试规范

- 使用 pytest 进行单元测试
- 测试覆盖率达到 80% 以上
- 集成测试覆盖主要业务流程
- 前端测试使用 Selenium 或 Cypress

## 部署规范

- 使用 Gunicorn 作为 WSGI 服务器
- 配置 Nginx 反向代理
- 使用 Docker 容器化部署
- 实现 CI/CD 自动化部署

## 版本控制规范

- 使用 Git 进行版本控制
- 遵循 Git Flow 工作流
- 提交信息使用约定式格式：`type(scope): description`
- 主要类型：feat, fix, docs, style, refactor, test, chore

---

**最后更新**: 2026-11-06
