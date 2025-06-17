import argparse

from predictor import DepthEstimationModel


def main():
    parser = argparse.ArgumentParser(description="Depth Estimation CLI Using ZoeDepth")
    parser.add_argument("input_image", help="Path to the input image file")
    parser.add_argument("output_image", help="Path to the output depth map")
    args = parser.parse_args()

    model = DepthEstimationModel()
    result = model.calculate_depthmap(args.input_image, args.output_image)
    print(f"Depth map saved to {result}")


if __name__ == "__main__":
    main()
