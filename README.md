# 免费社工库平台LosePrivacy源代码与API库 

## 什么是LosePrivacy

[LosePrivacy](https://loseprivacy.icu)收录了近10多年全球著名的数据泄露事件及数据，方便用户真实掌握：我们哪些隐私信息被泄露了、隐私信息被谁泄露了。

## loseprivacy-cli

LosePrivacy-cli可以让用户通过命令行快速查询社工库平台的数据，安全、高效。

LosePrivacy-cli主要是基于LosePrivacy API v1的部分接口完成。关于LosePrivacy API的详细描述请移步：[LosePrivacy API](https://loseprivacy.github.io)。

## 下载

```
git clone https://github.com/loseprivacy/loseprivacy-cli
cd loseprivacy-cli
```

### 配置
打开example.py，填入参数apikey即可。
apikey可以到LosePrivacy的开发者中心中获取。

## 使用样例

搜索QQ号

```
search_qq(keyword)
```

搜索用户名/姓名
```
search_username(keyword)
```

搜索密码
```
search_password(keyword)
```

搜索手机号
```
search_phone(keyword)
```

搜索身份证号
```
search_identity(keyword)
```

搜索微博
```
search_weiboid(keyword)
```

搜索邮箱
```
search_email(keyword)
```

搜索Facebook
```
search_facebook(keyword)
```

## 目前可搜索的部分裤子列表

- 17173网络游戏:17173网络游戏用户数据
- 人人网:人人网用户数据
- 12306:12306部分用户数据
- 天涯社区:天涯社区近4000万用户数据泄露
- 7K7K游戏:7K7K用户数据
- Taobao:Taobao近2000万用户数据泄露
- QQ:QQ用户数据
- 邮箱密码合集:多个安全事件中泄露的邮箱与密码数据合集
- 银行高存款客户:银行VIP用户数据
- 车主信息:70万车主信息数据
- 户籍信息:中国大陆1000多万居民户籍信息数据泄露
- Facebook:Facebook脸书超过5亿多用户数据泄露
- 借贷数据:暗网泄露的部分借贷数据
- 台湾居民信息:台湾2000多万居民敏感信息泄露
- BreachCompilation:14亿邮箱密码明文泄露信息合集
- 中国移动:中国移动多省份的用户信息泄露，涉及几千万用户
- 搜云:搜云社工库数据泄露
- 社保信息:38万深圳市社保数据泄露
- 平安保险:平安保险10万用户数据
- 小米论坛:小米论坛800万数据泄露
- 永硕E盘:永硕E盘用户数据
- 陌陌:陌陌3000万条数据泄露
- 京东:京东商城用户数据
- QQ密码:历年来泄露的QQ密码数据合集
- 手机密码合集:多个数据泄露事件中泄露的手机号与密码数据合集
- 华住集团酒店:华住集团酒店的用户数据
- 地下城与勇士DNF:地下城与勇士DNF近千万数据泄露
- 开心网:开心网用户数据
- 英雄联盟LoL:英雄联盟Lol共计1亿用户数据泄露
- Telegram:匿名聊天软件Telegram 4000多万用户数据泄露
- 顺丰快递:顺丰快递信息数据
- CSDN:CSDN账号数据
- 微博:微博用户数据
- 网易邮箱:网易邮箱数据
- 企查查:企查查全站数据
- QQ群:QQ群关系数据


