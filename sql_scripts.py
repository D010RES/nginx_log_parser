CREATE_LOGS_TBL = """ CREATE TABLE IF NOT EXISTS logs (
                                        ID integer PRIMARY KEY,                                        
                                        datetime text,
                                        client text,
                                        request_method text,
                                        request text,
                                        request_length text,
                                        status text,
                                        bytes_sent text,
                                        body_bytes_sent text,
                                        referer text,
                                        user_agent text,
                                        upstream_addr text,
                                        upstream_status text,
                                        request_time text,
                                        upstream_response_time text,
                                        upstream_connect_time text,
                                        upstream_header_time text
                                    ) """