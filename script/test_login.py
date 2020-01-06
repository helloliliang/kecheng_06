import unittest, logging,time
from api.login_api import LoginApi
from utils import assert_common


class TestIHRMLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # 初始化登录类
        cls.login_api = LoginApi()
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    # 成功登陆
    def test01_login_success(self):
        # 调用封装的登录接口
        response = self.login_api.login('13800000002', '123456')
        # 接收返回的json数据
        jsonData = response.json()
        # 调试输出登录接口返回的数据
        logging.info('登录成功返回的数据为：{}'.format(jsonData))
        # 断言
        # self.assertEqual(200, response.status_code)  # 断言响应状态码
        # self.assertEqual(True, jsonData.get('success'))  # 断言success的值
        # self.assertEqual(10000, jsonData.get('code'))  # 断言code
        # self.assertIn('操作成功', jsonData.get('message'))  # 断言message
        assert_common(self, response, 200, True, 10000, '操作成功')

    # 账号错误
    def test02_login_success(self):
        response = self.login_api.login('13900000002', '123456')
        jsonData = response.json()
        logging.info('登录成功返回的数据为：{}'.format(jsonData))
        assert_common(self, response, 200, False, 20001, '用户名或密码错误')

    # 密码错误
    def test03_login_success(self):
        response = self.login_api.login('13800000002', '12345')
        jsonData = response.json()
        logging.info('登录成功返回的数据为：{}'.format(jsonData))
        assert_common(self, response, 200, False, 20001, '用户名或密码错误')

    # 请求参数为空
    # def test04_login_success(self):
    #     response = self.login_api.login('', '')
    #     jsonData = response.json()
    #     logging.info('登录成功返回的数据为：{}'.format(jsonData))
    #     assert_common(self, response, 200, False, 99999, '抱歉，系统繁忙，请稍后重试!')

    # 账号为空
    def test05_login_success(self):
        response = self.login_api.login('', '123456')
        jsonData = response.json()
        logging.info('登录成功返回的数据为：{}'.format(jsonData))
        assert_common(self, response, 200, False, 20001, '用户名或密码错误')

    # 密码为空
    def test06_login_success(self):
        response = self.login_api.login('13800000002', '')
        jsonData = response.json()
        logging.info('登录成功返回的数据为：{}'.format(jsonData))
        assert_common(self, response, 200, False, 20001, '用户名或密码错误')
