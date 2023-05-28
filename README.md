# LLM-presets-flask-api
 An api used to create and read presets
本 Flask API 提供了两个端点以创建和读取预设。该 API 使用 GET 方法进行两个端点的操作。

## 用法

### 创建预设

端点：`/create`

#### 必需参数
- `preset`：字符串 - 要创建的预设的内容。
- `nickname`：字符串 - 创建预设的预设昵称。

#### 可选参数
- `from`：字符串 - 创建预设的用户名。

#### 请求示例
`GET /create?preset=这是一个测试预设&from=&nickname=test`

#### 响应示例
```
{
    "content": "这是一个测试预设",
    "nickname": "test",
    "preset_id": 1,
    "time": "2023-05-28 11:23:12",
    "uploader": "anonymous"
}
```

### 读取预设

端点：`/read`

#### 必需参数
- `id`：字符串 - 要读取的预设的 ID。

#### 请求示例
`GET /read?id=1`

#### 响应示例
```
{
    "content": "这是一个测试预设",
    "last_read_time": "2023-05-28 11:24:15",
    "nickname": "test",
    "preset_id": 1,
    "status": "ok",
    "time": "2023-05-28 11:23:12",
    "uploader": "anonymous"
}
```

## 注意事- 该 API 使用 `make_preset.py` 中的 `make_preset` 函数创建预设，使用 `read_preset.py` 中的 `read_preset` 函数读取预设。
- 该 API 运行在 `host='0.0.0.0'` 和 `port=7860` 上。请确保在发出请求时指定正确的主机和端口。
- 如果缺少任何必需参数，该 API 将返回 `400 Bad Request` 错误。
- `from` 参数是可选的。如果未提供该参数，则默认情况下将由匿名用户创建预设。
- 当读取预设时，`last_read_time` 字段将自动添加到响应中，指示最近一次读取预设的时间。
- 该 API 仅支持 GET 方法。
