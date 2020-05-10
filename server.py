from concurrent import futures
import logging

import grpc

import poisson_predictor_pb2
import poisson_predictor_pb2_grpc

import poisson_predictor


class PoissonPredictorServicer(poisson_predictor_pb2_grpc.PoissonPredictorServicer):
    def PredictOnAvePairScores(self, request, context):
        odds = poisson_predictor.predict_on_ave_pair_scores(
            request.ave_home_scored, request.ave_away_scored
        )
        return poisson_predictor_pb2.PredictionResponse(odds=odds)

    def PredictOnAveTeamScores(self, request, context):
        odds = poisson_predictor.predict_on_ave_team_scores(
            request.ave_scored_home,
            request.ave_conceded_home,
            request.ave_scored_away,
            request.ave_conceded_away,
        )
        return poisson_predictor_pb2.PredictionResponse(odds=odds)


def serve():

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    poisson_predictor_pb2_grpc.add_PoissonPredictorServicer_to_server(
        PoissonPredictorServicer(), server
    )
    print("Starting Poisson Predictor service on port 50051.")
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
