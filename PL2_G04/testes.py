import unittest
import primos
import game_of_life

class TestProjetoCPD(unittest.TestCase):

    def test_is_prime(self):
        """Valida a lógica base da função is_prime."""
        self.assertTrue(primos.is_prime(7))
        self.assertTrue(primos.is_prime(13))
        self.assertFalse(primos.is_prime(4))
        self.assertFalse(primos.is_prime(15))
        self.assertFalse(primos.is_prime(1))

    def test_primos_consistencia(self):
        """Verifica se o paralelo encontra um número válido."""
        timeout = 1
        res_seq = primos.find_max_prime_sequential(timeout)
        res_par = primos.find_max_prime_parallel(timeout, 2)
        self.assertTrue(primos.is_prime(res_seq))
        self.assertTrue(primos.is_prime(res_par))

    def test_game_of_life_block(self):
        """Teste com o padrão 'Block'."""
        block_grid = [
            [0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0]
        ]
        res_seq = game_of_life.game_of_life_sequential(block_grid, 2)
        res_par = game_of_life.game_of_life_parallel(block_grid, 2, 2)
        self.assertEqual(res_seq, block_grid)
        self.assertEqual(res_par, block_grid)
        self.assertEqual(res_seq, res_par)

    def test_game_of_life_consistencia(self):
        """Verifica se Seq e Par produzem o mesmo resultado."""
        random_grid = [
            [0, 1, 0, 0, 0],
            [1, 1, 1, 0, 0],
            [0, 1, 0, 1, 1],
            [0, 0, 0, 1, 1],
            [1, 1, 0, 0, 0]
        ]
        generations = 3
        res_seq = game_of_life.game_of_life_sequential(random_grid, generations)
        res_par = game_of_life.game_of_life_parallel(random_grid, generations, 2)
        self.assertEqual(res_seq, res_par)

if __name__ == "__main__":
    unittest.main()