import numpy as np


input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]


def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    else:
        # Create 3x3 matrix
        matrix = np.array(list).reshape(3, 3)
        # Mean
        df_mean_x = np.mean(matrix, axis=0).tolist()
        df_mean_y = np.mean(matrix, axis=1).tolist()
        df_mean_z = np.mean(matrix)
        # Variance
        df_var_x = np.var(matrix, axis=0).tolist()
        df_var_y = np.var(matrix, axis=1).tolist()
        df_var_z = np.var(matrix)
        # Standard Deviation
        df_std_x = np.std(matrix, axis=0).tolist()
        df_std_y = np.std(matrix, axis=1).tolist()
        df_std_z = np.std(matrix)
        # Max
        df_max_x = np.max(matrix, axis=0).tolist()
        df_max_y = np.max(matrix, axis=1).tolist()
        df_max_z = np.max(matrix)
        # Min
        df_min_x = np.min(matrix, axis=0).tolist()
        df_min_y = np.min(matrix, axis=1).tolist()
        df_min_z = np.min(matrix)
        # Sum
        df_sum_x = np.sum(matrix, axis=0).tolist()
        df_sum_y = np.sum(matrix, axis=1).tolist()
        df_sum_z = np.sum(matrix)

        calculations = {
            "mean": [df_mean_x, df_mean_y, df_mean_z],
            "variance": [df_var_x, df_var_y, df_var_z],
            "standard deviation": [df_std_x, df_std_y, df_std_z],
            "max": [df_max_x, df_max_y, df_max_z],
            "min": [df_min_x, df_min_y, df_min_z],
            "sum": [df_sum_x, df_sum_y, df_sum_z],
        }

        return calculations
