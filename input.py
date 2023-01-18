from datetime import datetime, timedelta
import unittest
import os
from app import create_app, db
from app.models import *
from config import Config


class TestConfig(Config):
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "app.db")


class UserModelCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_contex = self.app.app_context()
        self.app_contex.push()
        # self.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        # basedir = os.path.abspath(os.path.dirname(__file__))
        # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        db.create_all()

    def test_password_hashing(self):
        u = User(username="susan")
        u.set_password("susan1234")
        self.assertFalse(u.check_password("iloveyou1234"))
        self.assertTrue(u.check_password("susan1234"))

    def test_add_data(self):
        # User table
        u1 = User(
            username="Alice",
            email="alice@unittest.com",
            phone_no="123456780",
            birthday=datetime(2017, 3, 29),
            gender="female",
            profile_pic="https://randomuser.me/api/portraits/women/34.jpg",
        )
        u1.set_password("Susan1234")

        u2 = User(
            username="Bob",
            email="bob@unittest.com",
            phone_no="76453210",
            birthday=datetime(1957, 7, 9),
            gender="male",
            profile_pic="https://randomuser.me/api/portraits/men/34.jpg",
        )
        u2.set_password("Boby1234")

        u3 = User(
            username="Phuc",
            email="phuc@unittest.com",
            phone_no="0964383296",
            birthday=datetime(2002, 7, 9),
            gender="male",
        )
        u3.set_password("Phuc1234")
        db.session.add_all([u1, u2, u3])

        self.assertEqual(u1.username, "Alice")
        self.assertNotEqual(u2.username, "not_bob")

        # Reset_password_email table
        email1 = Reset_password_email(email="alice@unittest.com")
        email2 = Reset_password_email(email="bob@unittest.com")
        db.session.add_all([email1, email2])

        # Review table
        review1 = Review(
            user_id=1, shop_id=1, stars=3, comments="average", review_type="shop"
        )
        review2 = Review(
            user_id=2, shop_id=2, stars=4, comments="very good", review_type="shop"
        )
        review3 = Review(
            user_id=2, raucu_id=1, stars=1, comments="bad", review_type="raucu"
        )
        review4 = Review(
            user_id=2, raucu_id=2, stars=5, comments="perfect", review_type="raucu"
        )
        review5 = Review(
            user_id=1, shop_id=3, stars=3, comments="average", review_type="shop"
        )
        review6 = Review(
            user_id=2, shop_id=4, stars=4, comments="very good", review_type="shop"
        )
        review7 = Review(
            user_id=2, raucu_id=3, stars=3, comments="Vào mục nào để mình tặng tiền cho số điện thoại của người thân mua hàng. Hôm trước bhx có chỗ mình 40k để tặng số điện thoại mà chưa nhập giờ ko biết ở 3", review_type="raucu"
        )
        review8 = Review(
            user_id=2, raucu_id=4, stars=2, comments="Xà lách sao mà xấu quá, hư vàng bên ngoài lặt bỏ nhiều quá có lẽ do mưa nên rau kg ngon.", review_type="raucu"
        )
        review9 = Review(
            user_id=1, raucu_id=5, stars=4, comments="Rau xanh ăn rất ngon và rẻ nữa.", review_type="raucu"
        )
        review10 = Review(
            user_id=1, raucu_id=6, stars=3, comments="Hành củ vừa, ok. Có tầm 3 củ nảy mầm với hỏng thôi. Số lượng ít không đáng kể. Không cần gọi cho mình chăm sóc đâu 😅", review_type="raucu"
        )
        review11 = Review(
            user_id=2, raucu_id=7, stars=2, comments="Nấm dai ngon, không bị hôi, mua thêm mấy loại nấu lẩu nấm cũng ổn phết.", review_type="raucu"
        )
        review12 = Review(
            user_id=1, raucu_id=8, stars=2, comments="Nấm dai ngon, không bị hôi, mua thêm mấy loại nấu lẩu nấm cũng ổn phết.", review_type="raucu"
        )
        review13 = Review(
            user_id=2, raucu_id=11, stars=2, comments="Nấm dai ngon, không bị hôi, mua thêm mấy loại nấu lẩu nấm cũng ổn phết.", review_type="raucu"
        )
        review14 = Review(
            user_id=1, raucu_id=12, stars=2, comments="Nấm dai ngon, không bị hôi, mua thêm mấy loại nấu lẩu nấm cũng ổn phết.", review_type="raucu"
        )
        review15 = Review(
            user_id=2, raucu_id=13, stars=2, comments="Nấm dai ngon, không bị hôi, mua thêm mấy loại nấu lẩu nấm cũng ổn phết.", review_type="raucu"
        )
        review16 = Review(
            user_id=1, raucu_id=14, stars=2, comments="Nấm dai ngon, không bị hôi, mua thêm mấy loại nấu lẩu nấm cũng ổn phết.", review_type="raucu"
        )
        review17 = Review(
            user_id=2, raucu_id=15, stars=2, comments="Nấm dai ngon, không bị hôi, mua thêm mấy loại nấu lẩu nấm cũng ổn phết.", review_type="raucu"
        )
        review18 = Review(
            user_id=1, raucu_id=16, stars=2, comments="Nấm dai ngon, không bị hôi, mua thêm mấy loại nấu lẩu nấm cũng ổn phết.", review_type="raucu"
        )
        review19 = Review(
            user_id=2, raucu_id=17, stars=2, comments="Nấm dai ngon, không bị hôi, mua thêm mấy loại nấu lẩu nấm cũng ổn phết.", review_type="raucu"
        )
        review20 = Review(
            user_id=1, raucu_id=17, stars=2, comments="Mấy ngày ăn chay mua nấm này dìa ăn nè, ăn ngon mà không bị ngán nữa.", review_type="raucu"
        )
        review21 = Review(
            user_id=1, raucu_id=18, stars=2, comments="Mấy ngày ăn chay mua nấm này dìa ăn nè, ăn ngon mà không bị ngán nữa.", review_type="raucu"
        )
        review22 = Review(
            user_id=1, raucu_id=19, stars=2, comments="Mấy ngày ăn chay mua nấm này dìa ăn nè, ăn ngon mà không bị ngán nữa.", review_type="raucu"
        )
        review23 = Review(
            user_id=1, raucu_id=20, stars=2, comments="Mấy ngày ăn chay mua nấm này dìa ăn nè, ăn ngon mà không bị ngán nữa.", review_type="raucu"
        )
        review24 = Review(
            user_id=1, raucu_id=21, stars=2, comments="Mấy ngày ăn chay mua nấm này dìa ăn nè, ăn ngon mà không bị ngán nữa.", review_type="raucu"
        )
        review25 = Review(
            user_id=1, raucu_id=22, stars=2, comments="Mấy ngày ăn chay mua nấm này dìa ăn nè, ăn ngon mà không bị ngán nữa.", review_type="raucu"
        )
        review26 = Review(
            user_id=1, raucu_id=23, stars=2, comments="Mấy ngày ăn chay mua nấm này dìa ăn nè, ăn ngon mà không bị ngán nữa.", review_type="raucu"
        )
        review27 = Review(
            user_id=1, raucu_id=24, stars=2, comments="Mấy ngày ăn chay mua nấm này dìa ăn nè, ăn ngon mà không bị ngán nữa.", review_type="raucu"
        )
        review28 = Review(
            user_id=1, raucu_id=25, stars=2, comments="Mấy ngày ăn chay mua nấm này dìa ăn nè, ăn ngon mà không bị ngán nữa.", review_type="raucu"
        )
        review29 = Review(
            user_id=1, raucu_id=26, stars=2, comments="Mấy ngày ăn chay mua nấm này dìa ăn nè, ăn ngon mà không bị ngán nữa.", review_type="raucu"
        )
        review30 = Review(
            user_id=1, raucu_id=27, stars=2, comments="Mấy ngày ăn chay mua nấm này dìa ăn nè, ăn ngon mà không bị ngán nữa.", review_type="raucu"
        )
        review31 = Review(
            user_id=1, raucu_id=27, stars=2, comments="Mấy ngày ăn chay mua nấm này dìa ăn nè, ăn ngon mà không bị ngán nữa.", review_type="raucu"
        )
        review32 = Review(
            user_id=1, raucu_id=28, stars=2, comments="Mấy ngày ăn chay mua nấm này dìa ăn nè, ăn ngon mà không bị ngán nữa.", review_type="raucu"
        )
        review33 = Review(
            user_id=1, raucu_id=29, stars=2, comments="Mấy ngày ăn chay mua nấm này dìa ăn nè, ăn ngon mà không bị ngán nữa.", review_type="raucu"
        )
        review34 = Review(
            user_id=1, raucu_id=30, stars=2, comments="Mấy ngày ăn chay mua nấm này dìa ăn nè, ăn ngon mà không bị ngán nữa.", review_type="raucu"
        )
        review35 = Review(
            user_id=1, raucu_id=31, stars=2, comments="Mấy ngày ăn chay mua nấm này dìa ăn nè, ăn ngon mà không bị ngán nữa.", review_type="raucu"
        )
        review36 = Review(
            user_id=1, raucu_id=32, stars=2, comments="Mấy ngày ăn chay mua nấm này dìa ăn nè, ăn ngon mà không bị ngán nữa.", review_type="raucu"
        )
        review37 = Review(
            user_id=1, raucu_id=33, stars=2, comments="Mấy ngày ăn chay mua nấm này dìa ăn nè, ăn ngon mà không bị ngán nữa.", review_type="raucu"
        )
        review38 = Review(
            user_id=1, raucu_id=34, stars=2, comments="Mấy ngày ăn chay mua nấm này dìa ăn nè, ăn ngon mà không bị ngán nữa.", review_type="raucu"
        )
        review39 = Review(
            user_id=1, raucu_id=35, stars=2, comments="Mấy ngày ăn chay mua nấm này dìa ăn nè, ăn ngon mà không bị ngán nữa.", review_type="raucu"
        )
        review40 = Review(
            user_id=1, raucu_id=36, stars=2, comments="Mấy ngày ăn chay mua nấm này dìa ăn nè, ăn ngon mà không bị ngán nữa.", review_type="raucu"
        )
        review41 = Review(
            user_id=2, raucu_id=3, stars=2, comments="Mấy ngày ăn chay mua nấm này dìa ăn nè, ăn ngon mà không bị ngán nữa.", review_type="raucu"
        )
        review42 = Review(
            user_id=2, raucu_id=9, stars=2, comments="Nấm dai ngon, không bị hôi, mua thêm mấy loại nấu lẩu nấm cũng ổn phết.", review_type="raucu"
        )
        review43 = Review(
            user_id=2, raucu_id=10, stars=2, comments="Nấm dai ngon, không bị hôi, mua thêm mấy loại nấu lẩu nấm cũng ổn phết.", review_type="raucu"
        )
        review44 = Review(
            user_id=2, raucu_id=37, stars=2, comments="Mấy ngày ăn chay mua nấm này dìa ăn nè, ăn ngon mà không bị ngán nữa.", review_type="raucu"
        )
        review45 = Review(
            user_id=2, raucu_id=38, stars=2, comments="Mấy ngày ăn chay mua nấm này dìa ăn nè, ăn ngon mà không bị ngán nữa.", review_type="raucu"
        )
        db.session.add_all([review1, review2, review3, review4, review5, review6])
        db.session.add_all([review7, review8, review9, review10, review11, review12])
        db.session.add_all([review13, review14, review15, review16, review17])
        db.session.add_all([review18, review19, review20, review21])
        db.session.add_all([review22, review23, review24, review25])
        db.session.add_all([review26, review27, review28, review29])
        db.session.add_all([review30, review31, review32, review33])
        db.session.add_all([review34, review35, review36, review37])
        db.session.add_all([review38, review39, review40, review41])
        db.session.add_all([review42, review43, review44, review45])


        # Shop table
        shop1 = Shop(
            name="Bách hoá xanh",
            address="09 Nguyễn Quý Yêm, Khu phố 4, phường An Lạc, quận Bình Tân, Thành phố Hồ Chí Minh",
            phone_no="123456780",
            profile_pic="https://simg.zalopay.com.vn/zlp-website/assets/bach_hoa_xanh_khuyen_mai_1_da6a8c8243.jpg",
            no_selling=10,
            no_sold=5,
        )
        shop2 = Shop(
            name="Rau củ xanh offical",
            address="78-80-82 Tản Đà, Phường 11, Quận 5, Thành phố Hồ Chí Minh",
            profile_pic="https://cdn-icons-png.flaticon.com/512/2329/2329865.png",
            phone_no="4192.456.809",
            no_selling=105,
            no_sold=55,
        )
        shop3 = Shop(
            name="Big C Online",
            address="268 Tô Hiến Thành, Phường 15, Quận 10, TP. Hồ Chí Minh ( Ngã ba Tô Hiến Thành - Sư Vạn Hạnh)",
            profile_pic="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Big_C_Logo.svg/1200px-Big_C_Logo.svg.png",
            phone_no="0283.86.32.990",
            no_selling=91826,
            no_sold=1293746,
        )
        shop4 = Shop(
            name="Co.opmart Online",
            address="199-205 Nguyễn Thái Học,. Phường Phạm Ngũ Lão, Quận 1, TP.HCM",
            profile_pic="https://upload.wikimedia.org/wikipedia/vi/f/fa/Logo_Co-opmart_2012.jpg",
            phone_no="1900.5555.68",
            no_selling=1984,
            no_sold=17685,
        )
        db.session.add_all([shop1, shop2, shop3, shop4])

        # Raucu table
        raucu1 = Raucu(
            name="Rau muống nước gói 500g",
            product_pic="https://cdn.tgdd.vn/Products/Images/8820/271529/bhx/rau-muong-nuoc-goi-500g-202205190833394619.jpg",
            raucu_type="rau",
            shop_id=1,
            price=10300,
            description="Rau muống nước được trồng và đóng gói theo những tiêu chuẩn nghiêm ngặt, bảo đảm các tiêu chuẩn xanh - sach, chất lượng và an toàn với người dùng. Rau muống nước giòn, ngọt, chứa nhiều dinh dưỡng đặc biệt là sắt nên thường được sử dụng cho các món xào, luộc hoặc nhúng lẩu.",
            discount=0.05,
        )
        raucu2 = Raucu(
            name="Ớt hiểm trái túi 50g",
            product_pic="https://cdn.tgdd.vn/Products/Images/8820/271666/bhx/ot-hiem-trai-tui-50g-202205181711028044.jpg",
            raucu_type="giavi",
            shop_id=2,
            price=7000,
            description="Ớt hiểm có vị cay nồng, thơm, kích thích vị giác của người ăn, ớt là một trong những gia vị không thể thiếu trong nấu ăn cũng như mâm cơm của người Việt. Ớt hiểm luôn giữ được độ tươi mỗi ngày, được nuôi trồng theo quy trình nghiêm ngặt, bảo đảm các chỉ tiêu về an toàn và chất lượng.",
            discount=0.2,
        )
        raucu3 = Raucu(
            name="Khoai môn túi 500g (1 củ)",
            product_pic="https://cdn.tgdd.vn/Products/Images/8785/230843/bhx/khoai-mon-tui-500g-1-cu-202205201542114062.jpg",
            raucu_type="cu",
            shop_id=2,
            price=27000,
            description="Củ khoai môn có hàm lượng chất xơ và nhiều loại vitamin, khoáng chất dồi dào rất cần thiết cho sức khỏe con người. Khoai môn có lớp vỏ ngoài màu nâu, phần thịt bên trong màu trắng kết hợp với nhiều đốm màu tím nhạt, có thể chế biến thành nhiều món ăn ngon, hấp dẫn.",
            discount=0.3,
        )
        raucu4 = Raucu(
            name="Táo Ninh Thuận hộp 1kg (25 - 30 trái)",
            product_pic="https://cdn.tgdd.vn/Products/Images/8788/270218/bhx/tao-ninh-thuan-tui-1kg-25-30-trai-202211040906562481.jpg",
            raucu_type="traicay",
            shop_id=3,
            price=27600,
            description="Táo xanh Ninh Thuận là trái cây đặc sản của vùng đất Phan Rang Ninh Thuận. Táo xanh hay táo ta, táo gai, tên khoa học Ziziphus mauritiana, là cây ăn quả nhiệt đới có nguồn gốc châu Phi. Khi ăn rửa sạch và ăn luôn vỏ, có vị ngọt thanh, giòn tan trong miệng. Quả ngon hơn khi chấm cùng muối ớt/muối tôm.",
            discount=0.1,
        )
        raucu5 = Raucu(
            name="Táo Gala mini Mỹ hộp 1kg ( 8 - 11 trái)",
            product_pic="https://cdn.tgdd.vn/Products/Images/8788/296233/bhx/tao-gala-mini-my-hop-1kg-8-11-trai-202211231410398998.jpg",
            raucu_type="traicay",
            shop_id=4,
            price=51000,
            description="Táo gala mini là trái cây nhập khẩu Mỹ, chất lượng an toàn.Táo dồi dào dưỡng chất, có vị ngọt và thanh mát rất thích hợp cho người ăn kiêng. Ngoài ra, nhiều nghiên cứu: ăn 2 quả táo mỗi ngày có thể giảm nguy cơ đột quỵ hoặc đau tim nếu nguyên nhân xuất phát từ cholesterol làm cứng động mạch",
            discount=0.09,
        )
        raucu6 = Raucu(
            name="Bưởi năm roi trái từ 1.3kg - 1.4kg",
            product_pic="https://cdn.tgdd.vn/Products/Images/8788/273343/bhx/buoi-nam-roi-trai-tu-13kg-14kg-202211041008117276.jpg",
            raucu_type="traicay",
            shop_id=1,
            price=27600,
            description="Bưởi năm roi là một trong những trái cây đặc sản nổi tiếng của Việt Nam. Bưởi có mùi hương thanh mát, lúc ăn bạn sẽ cảm nhận được sự hoà quyện xen lẫn giữa vị chua và vị ngọt. Bưởi 5 roi không chỉ ngon mà còn nhiều dưỡng chất tốt cho sức khoẻ, hệ miễn dịch và phù hợp cho người giảm cân và tiểu đường",
            discount=0.1,
        )
        raucu7 = Raucu(
            name="Cam canh túi 1kg (7 -12 trái)",
            product_pic="https://cdn.tgdd.vn/Products/Images/8788/234082/bhx/cam-canh-tui-1kg-7-12-trai-202301071200207019.jpg",
            raucu_type="traicay",
            shop_id=2,
            price=65000,
            description="Có màu sắc đẹp, tròn, chắc quả có, mỏng, múi căng mọng mang vị ngọt đậm đà, thơm ngon. Trong cam canh chứa rất nhiều vitamin và dinh dưỡng cần thiết cho thể. Ngoài giải khát, giải nhiệt hiệu quả, còn giúp tăng cường hệ miễn dịch, kiểm soát mức cholesterol, giúp trẻ hóa làn da,...",
            discount=0.1,
        )
        raucu8 = Raucu(
            name="Chuối sứ nải từ 1.5kg trở lên",
            product_pic="https://cdn.tgdd.vn/Products/Images/8788/270353/bhx/chuoi-su-song-nai-tu-15kg-tro-len-202211241020196715.jpg",
            raucu_type="traicay",
            shop_id=3,
            price=30000,
            description="Chuối sứ là trái cây chứa rất nhiều chất dinh dưỡng cần thiết cho cơ thể, hương vị bùi bùi ngọn dịu vô cùng hấp dẫn. Ngoài ăn trực tiếp chuối sứ còn có thể dùng chế biến nhiều món ăn ngon hấp dẫn như sinh tố, chè, bánh, kem, sữa,...Chuối ngon nhất khi bắt đầu xuất hiện đốm nâu.",
            discount=0.05,
        )
        raucu8 = Raucu(
            name="Dưa hấu đỏ trái từ 1.9kg trở lên",
            product_pic="https://cdn.tgdd.vn/Products/Images/8788/270325/bhx/dua-hau-do-trai-tu-18kg-tro-len-202211071104486894.jpg",
            raucu_type="traicay",
            shop_id=4,
            price=37600,
            description="Dưa hấu đỏ là trái cây nhiều nước và các vitamin, khoáng chất cần thiết, đặc biệt là ít calo và chất béo. Dưa hấu được xem là một sản phẩm thay thế cho nước uống thông thường. Dưa hấu ngọt khi có vỏ xanh đậm, cuống héo, đuôi quả có vùng vàng.",
            discount=0.1,
        )
        raucu9 = Raucu(
            name="Ổi nữ hoàng vỉ 1kg (4-5 trái)",
            product_pic="https://cdn.tgdd.vn/Products/Images/8788/270266/bhx/oi-nu-hoang-vi-1kg-4-5-trai-202211040913505719.jpg",
            raucu_type="traicay",
            shop_id=1,
            price=25600,
            description="Ổi nữ hoàng loại trái cây được ưa chuộng tại Việt Nam. Ổi Nữ Hoàng có phần thịt khá dày và ruột rất nhỏ ít hạt khi ăn vào sẽ có vị giòn, ngọt thanh kích thích ăn mãi không ngừng. Ổi ngon, giòn nhất khi trái chắc, xanh sáng, cầm nặng tay.",
            discount=0.1,
        )
        raucu10 = Raucu(
            name="Chuối già giống Nam Mỹ hộp 1kg",
            product_pic="https://cdn.tgdd.vn/Products/Images/8788/272140/bhx/chuoi-gia-giong-nam-my-hop-1kg-6-7-trai-202212021511433572.jpg",
            raucu_type="traicay",
            shop_id=2,
            price=28000,
            description="Chuối già Nam Mỹ là giống chuối cấy mô, có nguồn gốc từ Nam Mỹ nên có chất lượng tốt và hương vị ngon, ngọt hơn hẳn so với các sản phẩm chuối khác. Chuối già to trái, mướt, ngon và chất lượng. Chuối không bị dập khi giao",
            discount=0.35,
        )
        raucu11 = Raucu(
            name="Chanh dây hộp 500g",
            product_pic="https://cdn.tgdd.vn/Products/Images/8788/274197/bhx/chanh-day-hop-500g-4-6-trai-giao-ngau-nhien-trai-vua-chin-hoac-chin-gia-nhan-vo-nhe-202210200914195411.jpg",
            raucu_type="traicay",
            shop_id=3,
            price=20000,
            description="Chanh dây (Passiflora) là một loại trái cây nhiệt đới. Chanh chín có vỏ màu tím sang đậm dần. Ruột chanh vàng mọng nước. Có vị chua và mùi thơm được sử dụng nhiều trong pha chế và nấu ăn, chứa chất chống oxy hóa mạnh và nhiều loại vitamin tốt cho hệ tiêu hóa, tim mạch, tăng cường miễn dịch.",
            discount=0.05,
        )
        raucu12 = Raucu(
            name="Dừa xiêm gọt vỏ",
            product_pic="https://cdn.tgdd.vn/Products/Images/8788/284023/bhx/dua-xiem-got-vo-202211030846538211.jpg",
            raucu_type="traicay",
            shop_id=4,
            price=20000,
            description="Dừa xiêm gọt vỏ có trái to, nhiều nước. Nước dừa có vị ngọt thanh, đậm đà. Dừa là loại trái cây có tính mát, được rất nhiều người ưa chuộng và lựa chọn sử dụng. Dừa có cạnh thấp, mịn, màu đều là dừa nhiều nước.",
            discount=0.1,
        )
        raucu13 = Raucu(
            name="Dưa lưới tròn ruột cam trái từ 1.2kg trở lên",
            product_pic="https://cdn.tgdd.vn/Products/Images/8788/273734/bhx/dua-luoi-tron-ruot-cam-trai-tu-12kg-tro-len-202212191059532412.jpg",
            raucu_type="traicay",
            shop_id=1,
            price=75000,
            description="Là loại trái cây được rất nhiều người ưa thích vì màu sắc đẹp mắt và vị ngon ngọt, mang giá trị dinh dưỡng cao và nhiều công dụng tuyệt vời cho sức khỏe như ngừa ung thư, bổ mắt, chống viêm khớp và làm đẹp da… Dưa lưới ngon nhất khi phần cuống lõm tròn, có hình răng cưa.",
            discount=0.1,
        )
        raucu14 = Raucu(
            name="Cam vàng Úc túi 1kg (3-5 trái)",
            product_pic="https://cdn.tgdd.vn/Products/Images/8788/202933/bhx/cam-vang-uc-tui-1kg-3-5-trai-202211030940379556.jpg",
            raucu_type="traicay",
            shop_id=2,
            price=62000,
            description="Cam Vàng Úc là trái cây nhập khẩu từ Úc. Đạt tiêu chuẩn xuất khẩu toàn cầu. Cam ngọt thanh, thơm đặc trưng, màu vàng bắt mắt, tép cam mọng nước ít xơ. Cam vàng Úc chứa nhiều Vitamin C, tốt cho da, chống lão hóa, giảm Cholesterol, phục sức khỏe, tạo hồng huyết cầu, giảm căng thẳng",
            discount=0.1,
        )
        raucu15 = Raucu(
            name="Xoài Úc túi 1.2kg (2 - 3 trái)",
            product_pic="https://cdn.tgdd.vn/Products/Images/8788/274393/bhx/xoai-uc-tui-12kg-1-2-trai-202211071655488054.jpg",
            raucu_type="traicay",
            shop_id=3,
            price=66000,
            description="Xoài Úc là trái cây có nguồn gốc nhập khẩu chất lượng cao. Xoài Úc là loại trái cây phổ biến và được ưa chuộng tại Việt Nam với vị thanh ngọt và ngát hương thơm dễ chịu chịu hấp. Cam kết bán đúng khối lượng, bao bì sạch sẽ, an toàn.",
            discount=0,
        )
        raucu16 = Raucu(
            name="Mận An Phước hộp 1kg (10 - 14 trái)",
            product_pic="https://cdn.tgdd.vn/Products/Images/8788/270278/bhx/man-an-phuoc-hop-1kg-10-14-trai-202210241508258262.jpg",
            raucu_type="traicay",
            shop_id=4,
            price=42000,
            description="Mận An Phước chín đỏ mọng đẹp mắt, màu sắc hấp dẫn, vị chua ngọt vừa phải dễ chịu . Mận An Phước chứa nhiều vitamin, chất xơ và khoáng chất, mận ngọt, ngon nhất khi chín đỏ vừa, có xen chút trắng, quả chắc. Cam kết trái cây bán đúng khối lượng, chất lượng và an toàn.",
            discount=0.05,
        )
        raucu17 = Raucu(
            name="Rau húng quế gói 100g",
            product_pic="https://cdn.tgdd.vn/Products/Images/8820/299256/bhx/rau-hung-que-goi-100g-202212090839472632.jpg",
            raucu_type="rau",
            shop_id=4,
            price=6500,
            description="Rau húng quế có mùi thơm rất dễ chịu, đặc trưng và thường kết hợp với húng cây làm thành bộ đôi rau nêm góp mặt trong nhiều bữa ăn của gia đình Việt như: Phở bò, bò kho, hủ tiếu, tiết canh, các món luộc, nướng,... Ngoài ra, húng quế còn có thể dùng để hỗ trợ một số bệnh nhẹ như: cảm mạo, ho,...",
            discount=0,
        )
        raucu18 = Raucu(
            name="Rau diếp cá gói 100g",
            product_pic="https://cdn.tgdd.vn/Products/Images/8820/299258/bhx/rau-diep-ca-goi-100g-202212090834251743.jpg",
            raucu_type="rau",
            shop_id=4,
            price=7000,
            description="Rau diếp cá là loại rau thường được ăn sống để chấm thịt kho, cuốn bánh tráng,... Ngoài làm thực phẩm thì diếp cá còn là một vị thuốc đông y cực tốt để chữ trị một số bệnh nhẹ như táo bón, trĩ, hạ sốt,... Đặc biệt, diếp cá còn có thể giúp làm đẹp hiệu quả như: trị mụn, đẹp da,..",
            discount=0,
        )
        raucu19 = Raucu(
            name="Xà lách lô lô xanh gói 500g",
            product_pic="https://cdn.tgdd.vn/Products/Images/8820/271485/bhx/xa-lach-lo-lo-xanh-goi-500g-202205181607134610.jpg",
            raucu_type="rau",
            shop_id=4,
            price=20000,
            description="Rau xà lách lô lô xanh của Bách hóa Xanh được trồng tại Lâm Đồng và đóng gói theo những tiêu chuẩn nghiêm ngặt, bảo đảm các tiêu chuẩn xanh - sach. Xà lách lô lô nhiều chất xơ, hàm lượng dinh dưỡng cao, vị ngọt, giòn nên thường dùng làm rau ăn kèm cho các món cuốn",
            discount=0.05,
        )
        raucu20 = Raucu(
            name="Cải ngọt baby gói 300g",
            product_pic="https://cdn.tgdd.vn/Products/Images/8820/223330/bhx/cai-ngot-baby-goi-300g-202205181631113408.jpg",
            raucu_type="rau",
            shop_id=3,
            price=15000,
            description="Rau cải ngọt có vị ngọt thanh, phù hợp với việc chế biến nhiều món ăn khác nhau. Cải ngọt baby của Bách Hóa Xanh được sử dụng phổ biến trong các bữa ăn của người Việt. Chứa hàm lượng dinh dưỡng cao nên cải ngọt giúp phòng ngừa ung thư, hỗ trợ trị bệnh gout,...",
            discount=0.05,
        )
        raucu21 = Raucu(
            name="Rau mồng tơi baby gói 300g",
            product_pic="https://cdn.tgdd.vn/Products/Images/8820/223332/bhx/rau-mong-toi-baby-goi-300g-202205240838481864.jpg",
            raucu_type="rau",
            shop_id=2,
            price=13500,
            description="Rau mồng tơi là loại rau có hàm lượng calo và chất béo thấp, nhưng lại chứa lượng lớn vitamin, khoáng chất thiết yếu và các hợp chất chống oxy hóa giúp cho quá trình tiêu hóa diễn ra hiệu quả hơn và ngăn ngừa các vấn đề về đường ruột. Rau mồng tơi rất tốt cho phụ nữ mang thai và trẻ em.",
            discount=0,
        )
        raucu22 = Raucu(
            name="Rau thơm các loại gói 200g",
            product_pic="https://cdn.tgdd.vn/Products/Images/8820/271489/bhx/rau-thom-cac-loai-goi-200g-202205190840468779.jpg",
            raucu_type="rau",
            shop_id=1,
            price=13000,
            description="Rau thơm các loại tại Bách hoá XANH bao gồm rau rau diếp cá, rau quế, rau tía tô, rau húng,... Đây là loại rau thơm không thể thiếu giúp tạo thêm hương vị cho các món ăn như bánh xèo, bánh khọt, bánh ướt,... Rau thơm tại Bách hoá XANH tươi ngon, xanh mơn mởn.",
            discount=0.05,
        )
        raucu23 = Raucu(
            name="Hẹ lá gói 100g",
            product_pic="https://cdn.tgdd.vn/Products/Images/8820/271502/bhx/he-la-goi-100g-202205181648400182.jpg",
            raucu_type="rau",
            shop_id=4,
            price=5500,
            description="Hẹ lá là loại rau có hàm lượng dinh dưỡng cao, có tác dụng dược lý, được sử dụng rất nhiều trong các bài thuốc dân gian cũng như bữa ăn hàng ngày. Hẹ lá tươi, xanh, có mùi hăng nhẹ và được sử dụng trong nhiều món ăn ngon.",
            discount=0,
        )
        raucu24 = Raucu(
            name="Tía tô gói 100g",
            product_pic="https://cdn.tgdd.vn/Products/Images/8820/299255/bhx/tia-to-goi-100g-202212090844259068.jpg",
            raucu_type="rau",
            shop_id=3,
            price=6500,
            description="Tía tô là một loại rau ăn kèm với các món ăn của người Việt. Vị cay cay, chát nhẹ của loại rau này được rất nhiều người yêu thích. Ngoài là một loại thực phẩm thì tía tô còn có thể hỗ trợ điều vị một số bệnh như: giúp đầu óc tỉnh táo, giảm stress, giảm đau kháng viêm....",
            discount=0,
        )
        raucu25 = Raucu(
            name="Gừng gói 100g (1 - 2 củ)",
            product_pic="https://cdn.tgdd.vn/Products/Images/8820/299251/bhx/gung-goi-100g-1-2-cu-202212051006261881.jpg",
            raucu_type="giavi",
            shop_id=3,
            price=6000,
            description="Gừng là một loại củ có rất nhiều công dụng đối với chúng ta. Ngoài là gia vị trong nấu ăn hàng ngày, gừng có thể dùng trong làm đẹp, làm thuốc cũng cực tốt. Có thể kể đến một số lợi ích của gừng như: làm ấm cơ thể, trừ hàn, tiêu đàm, dịu ho, cầm máu,...",
            discount=0,
        )
        raucu26 = Raucu(
            name="Tỏi tím chùm 500g - 600g",
            product_pic="https://cdn.tgdd.vn/Products/Images/8820/301592/bhx/toi-tim-chum-500g-600g-202301091438564457.jpg",
            raucu_type="giavi",
            shop_id=4,
            price=33000,
            description="Chùm tỏi tím là một loại gia vị mà nhà nhà đều phải có trong gian bếp của mình. Chúng giúp tạo ra một món ăn ngon hơn, thơm hơn, kích thích vị giác,... Các thành phần trong tỏi không những cung cấp dưỡng chất rất tốt cho cơ thể mà còn có thể giúp hỗ trợ phòng ngừa một số bệnh khác.",
            discount=0,
        )
        raucu27 = Raucu(
            name="Tỏi cô đơn túi 300g",
            product_pic="https://cdn.tgdd.vn/Products/Images/8820/271536/bhx/toi-co-don-tui-300g-202205190846520270.jpg",
            raucu_type="giavi",
            shop_id=1,
            price=40000,
            description="Tỏi cô đơn là một gia vị không thể thiếu trong gian bếp của mỗi gia đình. Tỏi cô đơn được trồng tại Trung Quốc, theo quy trình công nghệ nghiêm ngặt, bảo đảm các chỉ tiêu về an toàn và chất lượng. Tỏi có hàm lượng dinh dưỡng cao, tăng cường sức miễn dịch cho người sử dụng",
            discount=0,
        )
        raucu28 = Raucu(
            name="Hành tím túi 300g",
            product_pic="https://cdn.tgdd.vn/Products/Images/8820/271665/bhx/hanh-tim-tui-300g-202205181645457566.jpg",
            raucu_type="giavi",
            shop_id=2,
            price=23000,
            description="Củ hành tím là gia vị không thể thiếu trong căn bếp của mỗi gia đình. Hành tím không chỉ giúp món ăn của bạn thêm đậm đà, hấp dẫn mà còn còn có công dụng trong việc chăm sóc sức khỏe. Trong hành tím có chứa rất nhiều chất dinh dưỡng tốt cho sức khỏe.",
            discount=0.06,
        )
        raucu29 = Raucu(
            name="Nghệ tươi",
            product_pic="https://centerforhealthreporting.org/wp-content/uploads/2020/05/chua-dau-da-day-bang-nghe-tuoi-tot-khong.jpg",
            raucu_type="giavi",
            shop_id=3,
            price=22000,
            description="Nghệ vàng tươi có vị đắng, mùi thơm hơi hắc, có tác dụng hành khí, phá huyết, thông kinh, chỉ thống, tiêu mủ, kháng viêm, liền sẹo. Các nghiên cứu gần đây đã xác định chính xác các thành phần hóa học có trong nghệ vàng tươi. Hoạt chất chính là Curcumin (tinh thể ánh tím, nâu đỏ), ngoài ra trong nghệ tươi còn có 1-5% tinh dầu có màu vàng nhạt, thơm, 1% cacbon không no, 5% paratolyl metylcacbinol và 1% long não hữu tuyến, curcumen, tinh bột, chất béo, canxi oxalat...",
            discount=0.05,
        )
        raucu30 = Raucu(
            name="Dưa leo baby khay 500g (8-10 trái)",
            product_pic="https://cdn.tgdd.vn/Products/Images/8785/271668/bhx/dua-leo-baby-500g-8-10-trai-202205201602083144.jpg",
            raucu_type="cu",
            shop_id=4,
            price=19900,
            description="Dưa leo baby trồng tại Lâm Đồng là một giống dưa mới, được trồng khá nhiều ở nước ta, đây là một loại rau củ rất ngon, gần như là quen thuộc trong tất cả bữa ăn ở mọi gia đình. Dưa leo chứa rất nhiều chất dinh dưỡng và vitamin rất tốt cho cơ thể. Dưa leo còn có thể dụng để làm đẹp cũng rất hiệu quả.",
            discount=0,
        )
        raucu31 = Raucu(
            name="Ớt chuông đỏ túi 300gr (1 - 2 trái)",
            product_pic="https://cdn.tgdd.vn/Products/Images/8785/275324/bhx/ot-chuong-do-tui-300gr-1-2-trai-202211281605091968.jpg",
            raucu_type="cu",
            shop_id=3,
            price=21500,
            description="Ớt chuông đỏ trồng tại Lâm Đồng có kích thước to và căng mọng... Ớt chuông đỏ này không có vị cay gắt như các loại ớt thông thường khác mà có vị giòn nên thích hợp cho các món xào, ăn sống. Loại ớt này còn chứa nhiều khoáng chất và vitamin tốt cho cơ thể.",
            discount=0,
        )
        raucu32 = Raucu(
            name="Cà chua beef khay 500g (2-4 trái)",
            product_pic="https://cdn.tgdd.vn/Products/Images/8785/271516/bhx/ca-chua-beef-tui-500g-3-4-trai-202205201606433629.jpg",
            raucu_type="cu",
            shop_id=2,
            price=22000,
            description="Cà chua là loại rau củ rất tốt cho sức khoẻ nhờ chứa nhiều dinh dưỡng đặc biệt là vitamin A, C, K ngoài ra loại quả này còn giúp làm đẹp da cho phái nữ rất tốt. Cà chua được trồng tại Lâm Đồng có thể ăn sống hoặc chế biến các món ăn cũng rất phù hợp.",
            discount=0,
        )
        raucu33 = Raucu(
            name="Khổ qua khay 500g (3-5 trái)",
            product_pic="https://cdn.tgdd.vn/Products/Images/8785/291352/bhx/kho-qua-khay-500g-3-5-trai-202209190819457591.jpg",
            raucu_type="cu",
            shop_id=1,
            price=18500,
            description="Khổ qua hay mướp đắng là thực phẩm quen thuộc trong thực đơn hàng tuần của các bà nội trợ. Trong khổ qua chứa rất nhiều vitamin và khoáng chất tốt cho cơ thể, giúp nâng cao chức năng miễn dịch, thanh nhiệt giải độc. Khổ qua có thể chế biến thành canh hoặc các món xào đều rất ngon.",
            discount=0,
        )
        raucu34 = Raucu(
            name="Bí xanh trái 400g - 500g",
            product_pic="https://cdn.tgdd.vn/Products/Images/8785/278284/bhx/bi-xanh-trai-500g-600g-202205201644341501.jpg",
            raucu_type="cu",
            shop_id=2,
            price=11500,
            description="Được nhiều chị em nội trợ chọn mua để chế biến thành các món ăn ngon cho gia đình. Ngoài làm thực phẩm, bí xanh còn có thể dùng trong đông y, có tác dụng lợi tiểu, mát gan, giải độc, làm đẹp da và giảm cân. Bí xanh có thể chế biến thành các món ăn như: luộc, xào, nấu canh đều rất ngon.",
            discount=0,
        )
        raucu35 = Raucu(
            name="Cà tím túi 500g (2 - 3 trái)",
            product_pic="https://cdn.tgdd.vn/Products/Images/8785/271468/bhx/ca-tim-tui-500g-2-3-trai-202205201549329553.jpg",
            raucu_type="cu",
            shop_id=3,
            price=17000,
            description="Cà tím được trồng tại Đà Lạt hay còn được gọi là cà dái dê, đây là một loại rau củ chế biến được thành rất nhiều món ăn thơm ngon như: hấp, xào, nướng, ăn sống,... mỗi dạng đều mang lại hương vị rất ngon. Trong cà tím chứa hàm lượng chất xơ vô cùng cao và giàu sắt rất tốt cho cơ thể.",
            discount=0.05,
        )
        raucu36 = Raucu(
            name="Củ dền túi 500g (2 - 5 củ)",
            product_pic="https://cdn.tgdd.vn/Products/Images/8785/271470/bhx/cu-den-tui-500g-2-5-cu-202205201702334471.jpg",
            raucu_type="cu",
            shop_id=3,
            price=15000,
            description="Củ dền trồng tại Lâm Đồng là một loại củ thường được các chị em nội trợ chọn vào menu hàng tuần. Củ dền chứa nhiều vitamin và khoáng chất giúp cải thiện sức khoẻ cho cơ thể. Củ dền có thể dùng chế biến thành các món ăn như canh hay có thể dùng để làm nước ép cũng rất ngon.",
            discount=0,
        )
        raucu37 = Raucu(
            name="Rau cải thìa 4KFarm gói 500g",
            product_pic="https://cdn.tgdd.vn/Products/Images/8820/267905/bhx/cai-thia-4kfarm-goi-500g-202205181535085802.jpg",
            raucu_type="rau",
            shop_id=2,
            price=14000,
            description="Cải thìa 4KFarm (hay cải bẹ trắng) còn có tên là bạch giới tử thuộc họ cải cùng họ với cải thảo, cải bẹ xanh. Đây là loại rau chứa nhiều thành phần dinh dưỡng dễ chế biến, ăn ngon miệng. Đặc biệt, rau cải thìa cũng mang đến nhiều lợi cho sức khỏe như phòng ngừa bệnh đục nhân mắt, ngăn ngừa ung thư,...",
            discount=0,
        )
        raucu38 = Raucu(
            name="Súp lơ trắng túi 500g - 600g (1 bông)",
            product_pic="https://cdn.tgdd.vn/Products/Images/8785/275320/bhx/bong-cai-trang-tui-500gr-1-bong-202205201613493458.jpg",
            raucu_type="rau",
            shop_id=2,
            price=31000,
            description="Bông cải trắng hay còn gọi là súp lơ trắng là một loại rau họ cải, có giá trị dinh dưỡng rất cao. Bông cải trắng có phần bông màu trắng gắn khít vào nhau, xốp và hơi dai mềm, bên ngoài có lớp lá bao bọc xung quanh, phiến lá cứng và dày. Bông cải trắng tươi ngon, chất lượng.",
            discount=0,
        )
        raucu39 = Raucu(
            name="Rau bắp cải trái tim túi 500g - 600g",
            product_pic="https://cdn.tgdd.vn/Products/Images/8785/275318/bhx/bap-cai-trai-tim-tui-500gr-1-2-bap-202205201556192988.jpg",
            raucu_type="rau",
            shop_id=2,
            price=18000,
            description="Bắp cải là nguyên liệu quen thuộc trong mỗi bữa ăn hằng ngày, có thể tìm được hàm lượng Vitamin A, B dồi dào có trong bắp cải, đặc biệt là các chất chống ung thư như Sulforaphane, Phenethyl isothiocyanate và Indol-33 carbino...",
            discount=0,
        )
        db.session.add_all([raucu1, raucu2, raucu3, raucu4, raucu5, raucu6, raucu7])
        db.session.add_all([raucu8, raucu9, raucu10, raucu11, raucu12, raucu13])
        db.session.add_all([raucu14, raucu15, raucu16, raucu17, raucu18, raucu19])
        db.session.add_all([raucu20, raucu21, raucu22, raucu23, raucu24, raucu25])
        db.session.add_all([raucu26, raucu27, raucu28, raucu29, raucu30, raucu31])
        db.session.add_all([raucu32, raucu33, raucu34, raucu35, raucu36])
        db.session.add_all([raucu37, raucu38, raucu39])

        # Bookmark table
        bookmark1 = Bookmark(user_id=1, raucu_id=1)
        bookmark2 = Bookmark(user_id=1, raucu_id=2)
        bookmark3 = Bookmark(user_id=2, raucu_id=1)
        bookmark4 = Bookmark(user_id=2, raucu_id=2)
        db.session.add_all([bookmark1, bookmark2, bookmark3, bookmark4])

        # Cart table
        cart1 = Cart(user_id=1, raucu_id=1, quantity=40)
        cart2 = Cart(user_id=1, raucu_id=2, quantity=13)
        cart3 = Cart(user_id=2, raucu_id=1, quantity=12)
        cart4 = Cart(user_id=2, raucu_id=2, quantity=11)
        db.session.add_all([cart1, cart2, cart3, cart4])

        # Notifications table

        # Selling_list table
        selling1 = Selling_list(
            shop_id=1, raucu_id=1, quantity=222, status="selling", item_sold=32
        )
        selling2 = Selling_list(
            shop_id=2, raucu_id=2, quantity=0, status="out_of_stock", item_sold=332
        )
        db.session.add_all([selling1, selling2])

        # Receipt table
        receipt1 = Receipt(
            user_id=1,
            shipping_cost=12000,
            shipping_addr="123 Le Van Sy P12 Q3 TPHCM",
            total_price=320000,
        )
        receipt2 = Receipt(
            user_id=2,
            shipping_cost=99000,
            shipping_addr="345 Le Van Sy P12 Q3 TPHCM",
            total_price=520000,
        )
        receipt3 = Receipt(
            user_id=2,
            shipping_cost=99000,
            shipping_addr="345 Le Van Sy P12 Q3 TPHCM",
            total_price=520000,
            order_status="dathanhtoan",
        )
        receipt4 = Receipt(
            user_id=2,
            shipping_cost=99000,
            shipping_addr="345 Le Van Sy P12 Q3 TPHCM",
            total_price=520000,
            order_status="dahuy",
        )
        receipt5 = Receipt(
            user_id=1,
            shipping_cost=99000,
            shipping_addr="345 Le Van Sy P12 Q3 TPHCM",
            total_price=520000,
            order_status="dathanhtoan",
        )
        db.session.add_all([receipt1, receipt2, receipt3, receipt4, receipt5])

        # Receipt_list table
        list_receipt1 = Receipt_list(receipt_id=1, raucu_id=1, quantity=2)
        list_receipt2 = Receipt_list(receipt_id=2, raucu_id=2, quantity=3)
        list_receipt3 = Receipt_list(receipt_id=3, raucu_id=1, quantity=4)
        list_receipt4 = Receipt_list(receipt_id=4, raucu_id=2, quantity=5)
        db.session.add_all([list_receipt1, list_receipt2, list_receipt3, list_receipt4])

        # commit
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        self.app_contex.pop()


if __name__ == "__main__":
    # app.config['TESTING'] = True
    unittest.main(verbosity=2)
