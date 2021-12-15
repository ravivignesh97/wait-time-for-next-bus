import unittest
import nextbus
class TestWaitTimeForNextBus(unittest.TestCase):

    def test_valid_check_main_service_healthcheck(self):
        self.assertEqual(nextbus.check_main_service_healthcheck('https://svc.metrotransit.org'), True)

    def test_invalid_check_main_service_healthcheck_with_invalid_url(self):
        self.assertNotEqual(nextbus.check_main_service_healthcheck('https://demo.metrotransit.org'), True)

    def test_valid_find_route_info_by_name(self):
        route_info=nextbus.find_route_info_by_name('METRO Blue line')
        self.assertEqual('Description' in route_info, True)

    def test_invalid_find_route_info_by_name(self):
        route_info=nextbus.find_route_info_by_name('test')
        self.assertEqual(route_info, None)


    def test_valid_get_direction_id_by_route_id(self):
        direction_id=nextbus.get_direction_id_by_route_id(903,'south')
        self.assertEqual(type(direction_id), str)

    def test_invalid_get_direction_id_by_route_id(self):
        direction_id=nextbus.get_direction_id_by_route_id(902,'central')
        self.assertEqual(type(direction_id), type(None))



    def test_valid_get_stop_code_by_route_and_direction_ids(self):
        stop_code=nextbus.get_stop_code_by_route_and_direction_ids(901,0,'Target Field Station Platform 1')
        self.assertEqual(type(stop_code), str)

    def test_invalid_get_stop_code_by_route_and_direction_ids(self):
        stop_code=nextbus.get_stop_code_by_route_and_direction_ids(123,0,'test')
        self.assertEqual(type(stop_code), type(None))


    def test_valid_get_wait_time_for_next_bus(self):
        waittime=nextbus.get_wait_time_for_next_bus(901,0,'TF1')
        self.assertEqual(type(waittime), str)

    def test_invalid_get_wait_time_for_next_bus(self):
        waittime=nextbus.get_wait_time_for_next_bus(901,0,'ABC')
        self.assertEqual(type(waittime), type(None))

    
    def test_valid_nextbusinfo(self):
        response=nextbus.nextbusinfo("METRO Blue line","Target Field Station Platform 1",'north')
        self.assertEqual(type(response), str)

    def test_invalid_nextbusinfo(self):
        response=nextbus.nextbusinfo("METRO Blue line","Target Field Station Platform 1",'west')
        self.assertEqual(response, "Response: direction not found")


if __name__ == '__main__':
    unittest.main()