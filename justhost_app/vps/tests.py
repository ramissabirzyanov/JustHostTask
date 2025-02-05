from django.test import TestCase, Client
from vps.models import VPS
from django.urls import reverse


class TestVPSList(TestCase):
    def setUp(self):
        self.client = Client()
        self.vps = VPS.objects.create(
            cpu=12, ram=128, hdd=1024, status='started'
        )

    def test_get_vps_list(self):
        response = self.client.get(reverse('vps_list'))
        self.assertEqual(response.status_code, 200)

    def test_post_create_vps(self):
        vps_count = VPS.objects.count()
        response = self.client.post(
            reverse('vps_create'), {
                "cpu": 2,
                "ram": 32,
                "hdd": 512,
                "status": "blocked",
            })
        self.assertEqual(response.status_code, 201)
        self.assertIn("uid", response.json())
        self.assertEqual(VPS.objects.count(), vps_count + 1)


class TestVPSDetailView(TestCase):
    def setUp(self):
        self.client = Client()
        self.vps = VPS.objects.create(
            cpu=2, ram=8, hdd=256, status='started'
        )
        self.uid = self.vps.uid

    def test_get_vps_detail(self):
        response = self.client.get(reverse('vps_detail', args=[self.uid]))
        self.assertEqual(response.status_code, 200)
        self.assertIn("uid", response.json())
        self.assertEqual(response.json()["status"], "started")

    def test_put_new_vps_status(self):
        response = self.client.put(
            reverse('vps_detail', args=[self.uid]),
            data={"status": "stopped"},
            content_type='application/json'
        )
        self.vps.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertFalse(VPS.objects.filter(status='started').exists())
        self.assertEqual(self.vps.status, 'stopped')
